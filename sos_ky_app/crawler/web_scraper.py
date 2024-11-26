from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager


class WebScraper:
    def __init__(self):
        self.driver = self._setup_driver()

    def _setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chrome_options)

    def navigate_to_page(self, search_term):
        self.driver.get("https://web.sos.ky.gov/ftucc/(S(g3tg30x0ioe0ihtiya01reb4))/search.aspx")
        input_field = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_SearchForm1_tOrgname")
        input_field.send_keys(search_term)
        
        submit_button = self.driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_SearchForm1_bSearch")
        submit_button.click()

        active_row_link = self.driver.find_element(
            By.XPATH, '//*[contains(@id, "ctl00_ContentPlaceHolder1")]//table//tr[@class="Activebg"][1]/td/a'
        )
        active_row_link.click()

    def get_page_source(self):
        return self.driver.page_source

    def quit(self):
        self.driver.quit()