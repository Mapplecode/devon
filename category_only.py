from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
from sys import platform
from selenium.webdriver.support.ui import Select

def getAllproductLink(driver,url):
    next = '/html/body/div[1]/div[1]/div/div/div[2]/div/div[3]/ol[1]/li[3]'
    next_found = True
    product_list = list()
    # try:
    driver.get(url)
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
        while next_found:
            time.sleep(1)
            pro_list = driver.find_elements(By.XPATH,'//a[@rel="product"]')
            for product in pro_list:
                print(product.text)
                p_source = product.get_attribute('href')
                print(p_source)
                product_list.append({"Name":product.text,'URL':p_source})
            try:
                nextbtn  =  driver.find_element(By.CLASS_NAME,'pagination-next')
                nextbtn.click()
            except Exception as e:
                print(e)
                next_found = False
    # except Exception as e:
    #     print(e)
    return product_list

driver = webdriver.Chrome(executable_path='/home/mapple/PycharmProjects/devon/chromedriver')
url = 'https://www.backontrack-uk.co.uk/'
productList = getAllproductLink(driver,url)

fields = ['Product Name', '', 'URL']
filename = "product_url.csv"
csvfile = open(filename,'a')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(fields)
for p_url in productList:
    print(p_url)
    data= eval(str(p_url))
    csvwriter.writerow([data['Name'],data['URL']])
csvfile.close()