from celery import shared_task
from crawler.web_scraper import WebScraper
from crawler.data_extractor import DataExtractor


@shared_task
def run_webscraper():
    search_term = "eagle"
    scraper = WebScraper()

    try:
        scraper.navigate_to_page(search_term)
        page_source = scraper.get_page_source()
        extractor = DataExtractor(page_source)
        data = extractor.extract_all_data()
    finally:
        scraper.quit()

    return data