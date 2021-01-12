from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from config import config 


driver = webdriver.Chrome(config['selenium']['chromeDriverPath'])
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(5)
assert "No results found." not in driver.page_source
driver.close()