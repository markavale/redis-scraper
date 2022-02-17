# Main script for executing python code
from helpers import Converter
import time, datetime
from core import Scraper

def main():
    url = "https://www.rappler.com/nation/elections/ferdinand-bongbong-marcos-jr-media-blitz-january-2022/"
    scraper = Scraper(url=url)
    print(scraper.get_title())
    print(scraper.relevant_links)



if __name__ == "__main__":
    print("Executed at", datetime.datetime.now().strftime("%Y-%m-%d at %M:%S%p"))
    print("*", "-----"*10,"*")
    t1 = time.perf_counter()

    main()

    t2 = time.perf_counter()
    print("*", "-----"*10, "*")
    print("Finished in", Converter.convert_sec_to_hr_min_sec(round(t2 - t1, 2)))