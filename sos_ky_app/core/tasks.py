from celery import shared_task
from crawler.web_scraper import WebScraper
from crawler.data_extractor import DataExtractor
from search.models import SearchQuery, SearchResult


@shared_task
def run_webscraper(search_query_id):
    query = SearchQuery.objects.get(id=search_query_id)
    scraper = WebScraper()

    try:
        scraper.navigate_to_page(query.search_term)
        page_source = scraper.get_page_source()
        extractor = DataExtractor(page_source)
        data = extractor.extract_all_data()

        SearchResult.objects.create(search_query=query, organization_name=query.search_term, result_data=data)
        query.status = 'completed'
        query.save()
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
    finally:
        scraper.quit()

    return data