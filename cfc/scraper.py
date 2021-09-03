from bs4 import BeautifulSoup as bs
import json
import re
import requests
import os
from pathlib import Path
from sklearn.feature_extraction.text import CountVectorizer
import nltk


class Scraper():
    '''
    A class to represent a scraped webpage.
    ...
    Attributes:
    -----------
    url : str
        url of primary webpage to be scraped
    
    response : str
        raw html of primary webpage to be scraped
    
    parser : str
        name of html parser to be used
    
    soup : bs4.BeautifulSoup
        parsed html of primary webpage to be scraped
    
    Methods
    -------
    parse_links():
        Returns a list of all links/paths parsed from html.
        
    external_links(links):
        Returns a dict containing a list of the external resource links
        extracted from the parsed_links() method.
    
    enumerate_hyperlinks(links):
        Returns a dict containing all hyperlinks hosted on the domain server
        extracted from the parsed_links() method.
        The hyperlinks are enumerated with the numbers as the dict keys and links
        as the dict values.
    
    parse_privacy_page():
        Returns a list with strings of text parsed from the privacy page.
        The privacy page link is obtained from the enumerate_hyperlinks() method.
    
    word_frequency_counter_skl():
        Returns a dict with all unique words extracted from the privacy page
        using the scikit-learn CountVectorizer method.
        Only includes words with 2 letters or more.
    
    word_frequency_counter_nltk():
        Returns a dict with all unique words extracted from the privacy page
        using the nltk.
        Includes words with 1 letter or more.
    
    ouput_json(data, filenamepath=None):
        Saves a .json file to the `./data/` folder.
    '''
    
    def __init__(self):
        '''
        No attributes initialized with the Class.
        '''
        pass


    def parse_links(self):
        '''
        Returns a list of all links/paths parsed from html.

        Args:
            html (str): Filepath of the html to be parsed #TODO#
            url (str): URL of the website to be parsed #TODO#

        Returns:
            links (list): List of all links parsed from the html or url
        '''
        
        self.url = "https://www.cfcunderwriting.com"
        self.response = requests.get(self.url).text
        self.parser = 'html.parser'
        self.soup = bs(self.response, self.parser)
        
        links = []
        for link in self.soup.find_all(('link', 'a'), {'href': True}):
            links.append(link['href'])
    
        for link in self.soup.find_all(("script", 'iframe'), {'src': True}):
            links.append(link['src'])
            
        for link in self.soup.find_all('div', {'class': 'img'}):
            links.append(link['style'])
            self.soup_social = self.soup.find(('div'), {'class': 'social'})
        
        return links


    def external_links(self, links):
        '''
        Returns a dict of all the external resource links.
        The function filters out links that include the domain
        name from the URL.

        Args:
            links (list): List of links to be filtered
            
        Returns:
            external_links (dict): Dict of all external links referenced in the index page.
        '''
        
        external_links = []
        for link in links:
            # Exclude links with domain `cfcunderwriting.com`
            if re.match(".*(cfcunderwriting\.com+)[?\.]?", link, re.I):
                continue
            
            # Include paths starting with `http://` or `https://`
            if re.match('^(http|https)://', link, re.I):
                external_links.append(link)    
                continue
            
            # Clean and include background-image source path
            elif re.match("^background-image: url\('.*'", link, re.I):
                p = re.compile("'(.*?)'")
                m = p.search(link)
                link = m.group().replace("'","")
                external_links.append(link) 
                continue
        
        # Remove links to social sites that were parsed and added to list of all links
        for link in self.soup_social.find_all(('link', 'a'), {'href': True}):
            external_links.remove(link['href'])
        
        return {"external_links": external_links}


    def enumerate_hyperlinks(self, links):
        '''
        Returns a dict of all hyperlinks on the index page.
        The function filters out links that exclude the domain
        name from the URL.

        Args:
        links (list): List of links to be filtered

        Returns:
        hyperlinks_enumerated (dict): Dict of all hyperlinks referenced in the index page.
                Links are enumerated with the numbers representing
                the dict keys and the links the dict values.
        '''
        
        hyperlinks = []
        for link in links:
            #  Exclude links with the following domain names
            if re.match(".*(cloudflare\.com+)[?\.]?", link, re.I):
                continue
            elif re.match(".*(googleapis\.com+)[?\.]?", link, re.I):
                continue
            elif re.match(".*(google\.com+)[?\.]?", link, re.I):
                continue
            
            #  Include links with domain `cfcunderwriting.com`
            if re.match(".*(cfcunderwriting\.com+)[?\.]?", link, re.I):
                hyperlinks.append(link)
                continue
            
            # Include paths starting with `http://` or `https://`
            if re.match('^(http|https)://', link, re.I):
                hyperlinks.append(link)
                continue
            
            # Include paths starting with `en-`
            elif re.match("^/en-", link, re.I):
                hyperlinks.append(link)
                continue
        
        # Save links as dict keys to remove duplicate links
        hyperlinks_dict = {}
        for i, link in enumerate(hyperlinks):
            # Update path names starting with `en-` to include domain as prefix
            if re.match("^/en-gb", link, re.I):
                hyperlinks_dict[link.replace('/en-gb/', 'https://www.cfcunderwriting.com/en-gb/')] = i
                continue
            else:
                hyperlinks_dict[link] = i
        
        # Enumerate all unique links
        self.hyperlinks_enumerated = {i: link for i, link in enumerate(hyperlinks_dict.keys())}
        return {'hyperlinks_enumerated': self.hyperlinks_enumerated}


    def parse_privacy_page(self):
        '''
        Returns a list with strings of text parsed from the privacy page.
        The privacy page link is obtained from the enumerate_hyperlinks() method.

        Args:
            html (str): Filepath of the html to be parsed #TODO#
            url (str): URL of the website to be parsed #TODO#
            
        Returns:
            section_texts (list): List of words strings parsed from the privacy page. 
        '''
        
        url = self.hyperlinks_enumerated[67]
        response = requests.get(url).text
        soup = bs(response, self.parser)
        # Main section filter to ignore text in footer
        main_section = soup.find(["main"])
        sections = main_section.find_all(["h2", "p"])
        section_texts = []
        for section in sections:
            section_text = section.text.replace('\n',' ').lower()
            # Removes section numbers (ie 4.2.1)
            section_text = re.sub(r"(-?\d+)((\.(-?\d+))+)?", ' ', section_text)
            section_text = section_text.replace('\xa0',' ')
            section_texts.append(section_text)
            continue
        return section_texts


    def word_frequency_counter_skl(self):
        '''
        Returns a dict with all unique words extracted from the privacy page
        using the scikit-learn CountVectorizer method.
        Only includes words with 2 letters or more.

        Args:
            corpus (list): List of words strings #TODO#
            
        Returns:
            word_frequencies (dict): Dict containing unique 2 or more letter words and their frequency counts. 
        '''
        
        corpus = self.parse_privacy_page()
        cv = CountVectorizer()
        cv_fit = cv.fit_transform(corpus)
        words = cv.get_feature_names()
        counts = cv_fit.toarray().sum(axis=0)
        word_frequencies = {word: int(counts[i]) for i, word in enumerate(words)}
        return {'word_frequencies': word_frequencies}


    def word_frequency_counter_nltk(self):
        '''
        Returns a dict with all unique words extracted from the privacy page
        using nltk.
        Includes words with 1 letter or more.

        Args:
            corpus (list): List of words strings #TODO#
            
        Returns:
            word_frequencies (dict): Dict containing unique 1 or more letter words and their frequency counts. 
        '''
        
        # word_tokenize() only accepts a string, not list of strings.
        corpus = ' '.join(self.parse_privacy_page())
        words = nltk.tokenize.word_tokenize(corpus)
        counts = nltk.FreqDist(words)

        word_frequencies = dict((word, int(freq)) for word, freq in counts.items() if word.isalpha())
        return {'word_frequencies': word_frequencies}


    def ouput_json(self, data, filenamepath=None):
        '''
        Saves the data dict as a `.json` file.

        Args:
            data (dict): Dict to be saved as a `.json` file.
            filenamepath (str): Default path name is `./<dict_name>.json`
            
        Returns:
            (None): .json file saved to the default or specified directory. 
        '''
        
        root_dir = Path(__file__).parents[0]
        
        if filenamepath is None:
            filenamepath = os.path.join(root_dir, list(data.keys())[0])
        
        with open(f'{filenamepath}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"saved {filenamepath}.json")
        return None
    

if __name__ == "__main__":
    print('Running scraper.py')
    s = Scraper()
    s.ouput_json(s.external_links(s.parse_links()))
    s.ouput_json(s.enumerate_hyperlinks(s.parse_links()))
    s.ouput_json(s.word_frequency_counter_skl())
    