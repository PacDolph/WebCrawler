# with a chromeDriver installed on computer, use selenium and beautifulsoup, scrape content from a given url.
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

# chrome diver


def scrape(driver_path, scrape_target):
    option = ChromeOptions()
    option.headless = True
    driver = Chrome(executable_path=driver_path, options=option)
    driver.get(scrape_target)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    print("The type of soup:", soup.type)
    driver.quit()

if __name__ == "__main__":
    scrape()