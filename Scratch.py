from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import json


def lambda_handler(event, context):
    options = ChromeOptions()
    #options.binary_location = '/opt/headless-chromium'
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')

    driver = Chrome('/opt/chromedriver', options=options)
    driver.get('https://www.google.com/')

    driver.close();
    driver.quit();
    myJson = {"heading":"Selenium Test Running on AWS(Lambda)",
              "Selenium Version":"3"
              }
    abc =  {
        'statusCode': 200,
        'body': json.dumps(myJson,skipkeys = True,
                         allow_nan = True,
                         indent = 6)
    }
    json_object = json.dumps(response, indent=4)
    return json_object

if __name__ == '__main__':
    lambda_handler(None,None)