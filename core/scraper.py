from bs4 import BeautifulSoup
from helpers import RegexPatternGenerator
from requests import request
import re


class Scraper(object):
    
    def __init__(self, url, regex_pattern=None):
        self.url = url
        self.status_code = None
        self.page_source = None
        self.scraper_request()
        self.relevant_links = self.extract_relevant_links_pattern(orig_regex_pattern=regex_pattern)

    def scraper_request(self):
        req = request(method="GET", url=self.url)
        self.status_code = req.status_code
        if self.status_code == 200:
            self.page_source = req.text
        else:
            self.page_source = None

    def get_title(self):
        if self.status_code == 200:
            soup = BeautifulSoup(self.page_source, "html.parser")
            title = soup.find("meta", {"property": "og:title"})
            if title is not None:
                if title.get("content") is not None and title.get("content") != "":
                    return title['content']
                else:
                    return None
            return None
        return None

    def extract_relevant_links_pattern(self, orig_regex_pattern=None) -> list:

        if orig_regex_pattern is None:
            regex_instance = RegexPatternGenerator(self.url)
            regex_pattern = regex_instance.regex_pattern
            regex_pattern = regex_pattern.replace("\\\\", "\\")
        else:
            regex_pattern = orig_regex_pattern

        if self.page_source is not None:
            soup = BeautifulSoup(self.page_source, "html.parser")
            item_elements = soup.find_all("a", href=True)
            hrefs = list(map(lambda x: x['href'], item_elements))
            relative_links = list(filter(lambda x: re.search(regex_pattern, x), hrefs))
            return relative_links

