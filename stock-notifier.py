from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

from config import config

def getChromeDriver(chromeDriverPath):
    driver = webdriver.Chrome(chromeDriverPath)
    return driver

def findGraphicsCardsOnEbuyer(retailerConfig, driver):
    driver.get(retailerConfig['site'])
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-box"))
        )
        element.clear()
        element.send_keys('RTX 3060')
        element.send_keys(Keys.ENTER)

        itemElement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-box"))
        )
    finally:
        driver.quit()

def main():
    # get the chrome driver for executing selenium code
    driver = getChromeDriver(config['selenium']['chromeDriverPath'])

    for retailer in config['retailers']:
        if(retailer['name']=='ebuyer'):
            findGraphicsCardsOnEbuyer(retailer, driver)
        else:
            pass


if __name__ == "__main__":
    main()

 