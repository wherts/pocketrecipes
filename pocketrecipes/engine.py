from pocketrecipes.scrapers.bon_appetit import BonAppetitScraper
from pocketrecipes.scrapers.ny_times import NYTCookingScraper

BON_APPETIT = "www.bonappetit.com"
NYT_COOKING = "cooking.nytimes.com"


def get_scraper(recipe_url):
    if BON_APPETIT in recipe_url:
        return BonAppetitScraper(recipe_url)
    elif NYT_COOKING in recipe_url:
        return NYTCookingScraper(recipe_url)
    else:
        return None


def scrape_recipe(recipe_url):
    scraper = get_scraper(recipe_url)
    if not scraper:
        return None

    title = scraper.get_title()
    scraper.get_instructions()
    return title

    # save the recipe object and return recipe name
