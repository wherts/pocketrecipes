import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, source_url):
        self.url = source_url
        page = requests.get(source_url)
        self.soup = BeautifulSoup(page.content, "html.parser")

    def get_title(self):
        raise NotImplementedError("Must implement this function")

    def get_ingredients(self):
        raise NotImplementedError("Must implement this function")

    def get_instructions(self):
        raise NotImplementedError("Must implement this function")
