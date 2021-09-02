import unittest
from cfc.scraper import Scraper as S


class TestScraper(unittest.TestCase):
    def test_parse_links(self):
        links = S().parse_links()
        self.assertIsInstance(links, list, "The `parse_links` method should return a `list`")
        self.assertIsInstance(links[0], str, "The `parse_links` method should return a `str` with a url or file path name for each element in the list")
        self.assertEqual(links[0], 'https://www.cfcunderwriting.com/en-gb/')
        self.assertEqual(links[5], 'https://www.cfcunderwriting.com/en-gb/')
        self.assertEqual(links[-1], "background-image: url('https://cfccorpsite.azureedge.net/cache/9/b/0/a/d/b/9b0adbf131c63661d836a600698a5ac48a1e90f0.png');")
        pass