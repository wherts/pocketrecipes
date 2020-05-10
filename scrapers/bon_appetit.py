from pocketrecipes.scrapers.scraper import Scraper

# https://www.bonappetit.com/recipe/salt-and-pepper-fish
# https://www.bonappetit.com/recipe/adult-mac-and-cheese


class BonAppetitScraper(Scraper):
    def __init__(self, source_url):
        super().__init__(source_url)

    def get_title(self):
        header_class = "post__header_container"

        header = self.soup.find("header", class_=header_class)
        if not header:
            header = self.soup.find("div", class_=header_class)

        return header.find("h1").text

    def get_ingredients(self):
        ingredients_list = self.soup.find_all(
            "div", class_="ingredients__text"
        )
        ingredients = []
        for i in ingredients_list:
            ingredients.append(i.text)

    def get_instructions(self):
        instructions_list = self.soup.find("div", class_="steps-wrapper")
        instructions = []
        for i in instructions_list.find_all("li", class_="step"):
            instructions.append(i.text)
