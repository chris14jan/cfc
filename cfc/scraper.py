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
    '''
    
    def __init__(self):
        '''
        '''
        
        pass


    def parse_links(self):
        '''
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


    def enumerate_hyperlinks(self,links):
        '''
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
        '''
        url = self.hyperlinks_enumerated[67]
        response = requests.get(url).text
        soup = bs(response, self.parser)
        main_section = soup.find(["main"])
        sections = main_section.find_all(["h2", "p"])
        section_texts = []
        for section in sections:
            section_text = section.text.replace('\n',' ').lower()
            section_text = re.sub(r"(-?\d+)((\.(-?\d+))+)?", ' ', section_text)
            section_text = section_text.replace('\xa0',' ')
            section_texts.append(section_text)
            continue
        return section_texts


    def word_frequency_counter_skl(self):
        '''
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
        '''
        corpus = ' '.join(self.parse_privacy_page())
        words = nltk.tokenize.word_tokenize(corpus)
        counts = nltk.FreqDist(words)

        word_frequencies = dict((word, int(freq)) for word, freq in counts.items() if word.isalpha())
        return {'word_frequencies': word_frequencies}


    def ouput_json(self, data, filenamepath=None):
        '''
        '''
        
        root_dir = Path(__file__).parents[0]
        
        if filenamepath is None:
            filenamepath = os.path.join(root_dir, "data", list(data.keys())[0])
        
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
    