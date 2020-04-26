import requests
from bs4 import BeautifulSoup

url = "https://cooking.nytimes.com/recipes/1020022-quick-lamb-ragu?action=click&module=Local%20Search%20Recipe%20Card&pgType=search&rank=1"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# get ingredients
ingredients_list = soup.find("ul", class_="recipe-ingredients")
for i in ingredients_list.find_all("li"):
    qty = i.find("span", class_="quantity").text.strip()
    name = i.find("span", class_="ingredient-name").text.strip()
    print("{qty} {name}".format(qty=qty, name=name))

# get recipe steps
steps = soup.find("ol", class_="recipe-steps")
for step in steps.find_all("li"):
    print(step.text)
