import csv
import requests
from src.spider import scraper


driver_path = 'dependencies/chromedriver.exe'
scrape_target = 'https://quotes.toscrape.com/js'
scraper.scrape(driver_path, scrape_target)

# get urls

# analyse content and filter out interested content

# processing