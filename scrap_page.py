from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

def product_details(driver,url):
    try:
        detailList = list()
        print(url)
        driver.get(str(url['URL']))
        time.sleep(2)
        product_name = driver.find_element(By.CLASS_NAME, 'p-name').text
        price = driver.find_element(By.CLASS_NAME, 'p-price').text
        option_container = driver.find_element(By.CLASS_NAME, 'productOptionsTableContainer')
        product_select = option_container.find_element(By.XPATH, '//select[@name="option[Size]"]')
        select = Select(option_container.find_element(By.XPATH, '//select[@name="option[Size]"]'))
        # print(product_select)
        options = product_select.find_elements(By.TAG_NAME, 'option')
        # count = 0
        for option in options:
            time.sleep(2)
            value = option.get_attribute('value')
            size = option.text
            try:
                size = str(size).split('(')[0]
            except:
                pass
            select.select_by_value(value)
            # sel.sdelect_by_index(count)
            status = ''
            status = driver.find_element(By.CLASS_NAME, 'stock_level_message').text
            price = driver.find_element(By.CLASS_NAME,'wdk_basket_qtytxt').find_element(By.TAG_NAME,'span').text

            if not status:
                status = "Available"
            # print("\n INFO ",[product_name,price,size,status])
            if 'Choose' not in size:
                detailList.append([product_name, price, size, status])
        return detailList
    except Exception as e:
        print(e)
        return list()


driver = webdriver.Chrome(executable_path='/home/mapple/PycharmProjects/devon/chromedriver')
url = dict()
url['URL'] = 'https://www.backontrack-uk.co.uk/ourshop/prod_7717179-Back-on-Track-Canine-AllRound-Coat-Nella.html'
details = product_details(driver,url)
for det in details:
    print(det)