from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path='/home/mapple/PycharmProjects/devon/chromedriver')

driver.get('https://www.backontrack-uk.co.uk/')
time.sleep(2)
cats = driver.find_element(By.CLASS_NAME,'sub-category--grid')
source_list = list()
product_list = list()
cats = cats.find_elements(By.TAG_NAME,'li')
for cat in cats:
    print(cat.text)
    source = cat.find_element(By.TAG_NAME,'a').get_attribute('href')
    print(source)
    source_list.append(source)
print(source_list)
for source in source_list:
    driver.get(source)
    time.sleep(1)
    pro_list = driver.find_elements(By.XPATH,'//a[@rel="product"]')
    for product in pro_list:
        print(product.text)
        p_source = product.get_attribute('href')
        print(p_source)
        product_list.append(p_source)

print(product_list)