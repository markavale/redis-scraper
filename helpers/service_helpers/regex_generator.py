from urllib.parse import urlparse
import re


class RegexPatternGenerator:
    
    def __init__(self, url):
        super(RegexPatternGenerator, self).__init__()
        self.url = url
        self.url_path = self.url_path_extractor()
        self.url_fqdn = self.get_url_fqdn()
        self.regex_pattern = self.regex_pattern_generator()
        
        
    def get_url_fqdn(self):
        
        url = urlparse(self.url)
        article_fqdn = url.hostname
        article_fqdn_split = article_fqdn.strip('www.')
        
        return article_fqdn_split
    
        
    def url_path_extractor(self):
        
        url = urlparse(self.url)
        article_path = url.path
        
        return article_path
    

    def regex_pattern_generator(self):
    
        if self.url_path is not None:   
            
            regex_pattern = []
            url_path_splits = self.url_path.split('/')
            clean_url_path = list(filter(lambda x: x != '', url_path_splits))
            # print(clean_url_path)

            for url_paths in clean_url_path:
                if url_paths.isdigit() and len(url_paths) <= 2:
                    a = r'\\d{1,2}' 
                    regex_pattern.append(a)
                elif url_paths.isdigit() and len(url_paths) == 4:
                    b = r'\\d{4}'
                    regex_pattern.append(b)
                elif url_paths.isdigit() and len(url_paths) >= 5:
                    c = r'\\d{5,10}'
                    regex_pattern.append(c)
                elif url_paths.isalnum():
                    d = r'(\\w+)'  
                    regex_pattern.append(d)
                elif url_paths.isalpha():
                    e = r'([a-zA-Z]*)'  
                    regex_pattern.append(e)
                elif re.match(r'((\w+)-(\w+)$)', url_paths):
                    h = r'(\\w+)-(\\w+)'
                    regex_pattern.append(h)
                elif re.match(r'(\w+)-', url_paths):
                    i = r'(\\w.+)'
                    regex_pattern.append(i)

            regex_join = r'\\/'.join(regex_pattern)
            regexes_join = r'\\/' + regex_join
            # regexes_join = r'\/' + regex_join + r'\/$'

            return regexes_join

        else:
            return None