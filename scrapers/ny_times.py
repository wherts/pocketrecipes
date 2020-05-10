from pocketrecipes.scrapers.scraper import Scraper

# https://cooking.nytimes.com/recipes/1020022-quick-lamb-ragu?action=click&module=Local%20Search%20Recipe%20Card&pgType=search&rank=1


class NYTCookingScraper(Scraper):
    def __init__(self, source_url):
        super().__init__(source_url)

    def get_title(self):
        return self.soup.find("h1", class_="recipe-title").text

    def get_ingredients(self):
        ingredients_list = self.soup.find("ul", class_="recipe-ingredients")
        ingredients = []
        for i in ingredients_list.find_all("li"):
            qty = i.find("span", class_="quantity").text.strip()
            name = i.find("span", class_="ingredient-name").text.strip()
            ingredients.append("{qty} {name}".format(qty=qty, name=name))

    def get_instructions(self):
        instructions_list = self.soup.find("ol", class_="recipe-steps")
        instructions = []
        for i in instructions_list.find_all("li"):
            instructions.append(i.text)
