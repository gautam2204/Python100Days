from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import json

from requests import head

dict_of_broken_urls = {}
list_of_notCallable_urls = []


def setup():
    options = ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    return Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)




def close_driver(driver):
    print("Closing the driver")
    driver.close()


def getAllUrls(driver):
    all_tags = driver.find_elements(By.XPATH, "//a")
    for tag in all_tags:
        url = tag.get_attribute("href")
        try:
            response = head(url=url)
            dict_of_broken_urls[url] = response
            if response.status_code >= 400:
                print(f" {url} ::: {response.status_code}")
        except Exception:
            list_of_notCallable_urls.append(url)


def launchBrowser(driver):
    driver.get("https://www.tiaa.org/public/")
    print(driver.title)


if __name__ == '__main__':
    driver = setup()
    launchBrowser(driver)
    getAllUrls(driver)
    close_driver(driver)
    json.dumps()