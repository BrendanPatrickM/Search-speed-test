from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/brendanmurray/Documents/Development/Drivers/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


def run_search():
    driver.get('https://www.redcross.org.uk/shop/find-a-charity-shop')
    location = driver.find_element(By.ID, 'location')
    location.send_keys('e107an')
    location.send_keys(Keys.ENTER)

run_search()
