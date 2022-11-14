from abc import ABC, abstractmethod
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import requests
import shutil


class DataExtractHandler(ABC):
    @abstractmethod
    def fetch_csv_link(self):
        pass

    @abstractmethod
    def download_content(self):
        pass


class DataScraper(DataExtractHandler):
    def __init__(self, data):
        self.endpoin = data["endpoint"]

    def fetch_csv_link(self) -> dict:
        # self.endpoin = 'http://reports.ieso.ca/public/Demand/'
        http = httplib2.Http()
        status, response = http.request(self.endpoin)
        file_names = []
        for link in BeautifulSoup(response, parse_only=SoupStrainer("a")):
            if link.has_attr("href"):
                csv_name = link["href"]
                file_names.append(csv_name)
                with open("csv_url.txt", "a+") as f:
                    f.write(f"{self.endpoin}{csv_name}\n")

        return file_names

    def dispatcher(self) -> dict:
        """
        :return:
        """
        for date in self.fetch_csv_link():
            url = self.endpoin + date + ".csv"
            csv_filename = date + ".csv"
            try:
                print("Calling url:- " + url)
                r = requests.get(url, stream=True)
                if r.status_code == 200:
                    with open(csv_filename, "wb") as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                r.close()
            except Exception as e:
                print(
                    "for Date "
                    + date
                    + "Exception happened, most probably a weekend, EXCEPTION Message is "
                    + str(e)
                )
