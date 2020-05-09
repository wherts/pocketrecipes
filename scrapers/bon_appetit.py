import requests
from bs4 import BeautifulSoup

url = "https://www.bonappetit.com/recipe/salt-and-pepper-fish"
# url = "https://www.bonappetit.com/recipe/adult-mac-and-cheese"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# get ingredients
ingredients = soup.find_all("div", class_="ingredients__text")
for i in ingredients:
    print(i.text)

# get steps
steps_wrapper = soup.find("div", class_="steps-wrapper")
for s in steps_wrapper.find_all("li", class_="step"):
    print(s.text)
