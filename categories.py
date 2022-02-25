from telnetlib import STATUS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv 
from sys import exec_prefix, platform
from selenium.webdriver.support.ui import Select


def product_details(driver,url):
    try:
        detailList = list()
        driver.get(url)
        time.sleep(2)
        product_name = driver.find_element(By.CLASS_NAME,'p-name').text
        price = driver.find_element(By.CLASS_NAME,'p-price').text
        select  = driver.find_element(By.CLASS_NAME,'optionSelect').text
        all_sizes = driver.find_element(By.CLASS_NAME,'optionSelect').text
        sizes = all_sizes.split('\n')
        sizes.pop(0)

        # count = 0
        for size in sizes[:-1]:
            sel = Select(driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/section/article/div/div[2]/div/div[2]/div/div[1]/form/div/table/tbody/tr[1]/td[2]/select'))
            time.sleep(2)
            sel.select_by_visible_text(size)
            # sel.select_by_index(count)
            status = ''
            status = driver.find_element(By.ID, 'stocklevel5310380').text
            if not status:
                status = "Available"
            print("\n INFO ",[product_name,price,size,status])
            detailList.append([product_name,price,size,status])
            # count += 1
        return detailList
    except Exception as e:
        return list()

def getAllproductLink(driver,url):
    try:
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
            time.sleep(1)
            pro_list = driver.find_elements(By.XPATH,'//a[@rel="product"]')
            for product in pro_list:
                print(product.text)
                p_source = product.get_attribute('href')
                print(p_source)
                product_list.append(p_source)
        # print(product_list)
        return product_list
    except Exception as e:
        return list()

def write_csv(rows,filename):
    fields = ['Product Name', 'Price', 'Size', 'Status'] 
    rows = rows

    with open(filename, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(fields) 
        csvwriter.writerows(rows)
    print("[INFO] File write successfully.")

def main():
    if platform == "linux" or platform == "linux2":
        # linux
        driver = webdriver.Chrome(executable_path='/home/mapple/PycharmProjects/devon/chromedriver')

    elif platform == "win32":
        # Windows...    
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s, options=options)  

    try:
        filename = "product_details.csv"

        ## call function        
        url = 'https://www.backontrack-uk.co.uk/'

        ## For all the urls
        # productList = getAllproductLink(driver,url)
        # for product_url in productList:
        #     productUrl = "https://www.backontrack-uk.co.uk/ourshop/prod_5310380-Back-on-Track-Canine-Fleece-RugSupreme.html"
        #     detailList = product_details(driver,productUrl)
        #     write_csv(detailList,filename)


        ## for single url
        productUrl = "https://www.backontrack-uk.co.uk/ourshop/prod_5310380-Back-on-Track-Canine-Fleece-RugSupreme.html"
        detailList = product_details(driver,productUrl)
        filename = "product_details.csv"
        write_csv(detailList,filename)

    except Exception as e:
        print(e)    


if __name__ == "__main__":
    main()

