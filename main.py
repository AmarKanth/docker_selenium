from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# set up Chrome driver
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://web.sos.ky.gov/ftucc/(S(g3tg30x0ioe0ihtiya01reb4))/search.aspx")

input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_SearchForm1_tOrgname")
input_field.send_keys("eagle")

submit_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_SearchForm1_bSearch")
submit_button.click()

active_row_link = driver.find_element(
	By.XPATH, '//table[@id="ctl00_ContentPlaceHolder1_searchlist2_Table1"]//tr[@class="Activebg"][1]/td/a'
)
active_row_link.click()

page_source = driver.page_source

soup = BeautifulSoup(page_source, "html.parser")

data = {}

data["file_number"] = soup.find(id="ctl00_ContentPlaceHolder1_showentity1_Filenumber").text.strip()
data["filing_date"] = soup.find(id="ctl00_ContentPlaceHolder1_showentity1_Filedate").text.strip()
data["lapse_date"] = soup.find(id="ctl00_ContentPlaceHolder1_showentity1_Lapsedate").text.strip()
data["status"] = soup.find(id="ctl00_ContentPlaceHolder1_showentity1_status").text.strip()

rows = soup.select('table#ctl00_ContentPlaceHolder1_showentity1_actionstable tr.Activebg')
actions = []
for row in rows:
    cols = row.find_all("td")
    action = cols[0].text.strip()
    file_date = cols[1].text.strip()
    status = cols[2].text.strip()
    actions.append({"Action": action, "File Date": file_date, "Status": status})
data["actions"] = actions

rows = soup.select('table#ctl00_ContentPlaceHolder1_showentity1_namestable tr.Activebg.CollBorder')
names = []
for row in rows:
    cols = row.find_all("td")
    name_role = cols[0].text.strip().replace('\n', ' - ')
    date_added = cols[1].text.strip()
    address = cols[2].text.strip().replace('<br>', ', ')
    names.append({"Name Role": name_role, "Date Added": date_added, "Address": address})
data["names"] = names

row = soup.select_one('table#ctl00_ContentPlaceHolder1_showentity1_collateraltable tr.Activebg.CollBorder')
date_filed = row.find_all("td")[0].text.strip()
description = row.find_all("td")[1].text.strip()
data["collateral_description"] = {"date_filed": date_filed, "description": description}


rows = soup.select('table#ctl00_ContentPlaceHolder1_showentity1_imagestable tr.Activebg')
images = []
for row in rows:
	cols = row.find_all("td")
	doc_type = cols[0].text.strip()
	link = cols[1].find("a")["href"] if cols[1].find("a") else None
	tiff_image = cols[2].text.strip()
	file_date = cols[3].text.strip()
	pages = cols[4].text.strip()
	images.append({"doc_type": doc_type, "link": link, "tiff_image": tiff_image, "file_date": file_date, "pages": pages})
data["images"] = images

print(data)

driver.quit()
