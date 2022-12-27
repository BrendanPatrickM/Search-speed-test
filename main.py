from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

source = "https://www.redcross.org.uk/shop/find-a-charity-shop"
driver_path = "/Users/brendanmurray/Documents/Development/Drivers/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

def run_search():
    driver.get(source)
    location = driver.find_element(By.ID, 'location')
    location.send_keys('e107an')
    location.send_keys(Keys.ENTER)
    print('in loop')
  

for i in range(7):
    print(f"start loop {i}")
    run_search()
    print(f"end loop {i}")
driver.close()
   

