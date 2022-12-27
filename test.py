from selenium import webdriver
import time

chrome_driver_path = "/Users/brendanmurray/Documents/Development/Drivers/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
source = "https://www.redcross.org.uk/shop/find-a-charity-shop"

driver.get(source)
navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart

print(f"Backend performance: {backendPerformance_calc}")
print(f"Frontend performance: {frontendPerformance_calc}")

driver.close()


