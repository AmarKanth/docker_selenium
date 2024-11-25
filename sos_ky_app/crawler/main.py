from web_scraper import WebScraper
from data_extractor import DataExtractor


if __name__ == "__main__":
    search_term = "eagle"
    scraper = WebScraper()

    try:
        scraper.navigate_to_page(search_term)
        page_source = scraper.get_page_source()
        extractor = DataExtractor(page_source)
        data = extractor.extract_all_data()
        print(data)
    finally:
        scraper.quit()
