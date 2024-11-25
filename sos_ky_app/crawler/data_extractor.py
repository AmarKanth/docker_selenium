from bs4 import BeautifulSoup


class DataExtractor:
    def __init__(self, page_source):
        self.soup = BeautifulSoup(page_source, "html.parser")

    def extract_basic_info(self):
        return {
            "file_number": self.soup.find(id="ctl00_ContentPlaceHolder1_showentity1_Filenumber").text.strip(),
            "filing_date": self.soup.find(id="ctl00_ContentPlaceHolder1_showentity1_Filedate").text.strip(),
            "lapse_date": self.soup.find(id="ctl00_ContentPlaceHolder1_showentity1_Lapsedate").text.strip(),
            "status": self.soup.find(id="ctl00_ContentPlaceHolder1_showentity1_status").text.strip()
        }

    def extract_actions(self):
        rows = self.soup.select('table#ctl00_ContentPlaceHolder1_showentity1_actionstable tr.Activebg')
        actions = [
            {
                "Action": row.find_all("td")[0].text.strip(),
                "File Date": row.find_all("td")[1].text.strip(),
                "Status": row.find_all("td")[2].text.strip()
            }
            for row in rows
        ]
        return actions

    def extract_names(self):
        rows = self.soup.select('table#ctl00_ContentPlaceHolder1_showentity1_namestable tr.Activebg.CollBorder')
        names = [
            {
                "Name Role": row.find_all("td")[0].text.strip().replace('\n', ' - '),
                "Date Added": row.find_all("td")[1].text.strip(),
                "Address": row.find_all("td")[2].text.strip().replace('<br>', ', ')
            }
            for row in rows
        ]
        return names

    def extract_collateral_description(self):
        row = self.soup.select_one('table#ctl00_ContentPlaceHolder1_showentity1_collateraltable tr.Activebg.CollBorder')
        if row:
            cols = row.find_all("td")
            return {
                "date_filed": cols[0].text.strip(),
                "description": cols[1].text.strip()
            }
        return None

    def extract_images(self):
        rows = self.soup.select('table#ctl00_ContentPlaceHolder1_showentity1_imagestable tr.Activebg')
        images = [
            {
                "doc_type": row.find_all("td")[0].text.strip(),
                "link": row.find_all("td")[1].find("a")["href"] if row.find_all("td")[1].find("a") else None,
                "tiff_image": row.find_all("td")[2].text.strip(),
                "file_date": row.find_all("td")[3].text.strip(),
                "pages": row.find_all("td")[4].text.strip()
            }
            for row in rows
        ]
        return images

    def extract_all_data(self):
        return {
            "basic_info": self.extract_basic_info(),
            "actions": self.extract_actions(),
            "names": self.extract_names(),
            "collateral_description": self.extract_collateral_description(),
            "images": self.extract_images()
        }