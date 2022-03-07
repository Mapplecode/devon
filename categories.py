from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv 
from sys import platform
from selenium.webdriver.support.ui import Select


def product_details(driver,url):
    try:
        detailList = list()
        print(url)
        driver.get(str(url['URL']))
        time.sleep(2)
        product_name = driver.find_element(By.CLASS_NAME, 'p-name').text
        price = driver.find_element(By.CLASS_NAME, 'p-price').text
        try:
            option_container = driver.find_element(By.CLASS_NAME, 'productOptionsTableContainer')
            loc = option_container.location_once_scrolled_into_view
            product_select = option_container.find_element(By.XPATH, '//select[@name="option[Size]"]')
            select = Select(option_container.find_element(By.XPATH, '//select[@name="option[Size]"]'))
            # print(product_select)
            options = product_select.find_elements(By.TAG_NAME, 'option')
            # count = 0
            for option in options:
                time.sleep(2)
                value = option.get_attribute('value')
                select.select_by_value(value)
                size = value
                try:
                    size = str(size).split('|')[0]
                except:
                    pass
                # sel.select_by_index(count)
                status = ''
                status = driver.find_element(By.CLASS_NAME, 'stock_level_message').text
                price = driver.find_element(By.CLASS_NAME, 'wdk_basket_qtytxt').find_element(By.TAG_NAME, 'span').text

                if not status:
                    status = "Available"
                # print("\n INFO ",[product_name,price,size,status])
                if 'Choose' not in size:
                    detailList.append([product_name, price, size, status])
                # count += 1
        except:
            status = driver.find_element(By.CLASS_NAME, 'stock_level_message').text
            price = driver.find_element(By.CLASS_NAME,'wdk_basket_qtytxt').text
            if not status:
                status = "Available"
            detailList.append([product_name, price.split(" ")[2], '', status])
        return detailList
    except Exception as e:
        print(e)
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
            next_found = True
            while next_found:
                time.sleep(1)
                pro_list = driver.find_elements(By.XPATH, '//a[@rel="product"]')
                for product in pro_list:
                    print(product.text)
                    p_source = product.get_attribute('href')
                    print(p_source)
                    product_list.append({"Name": product.text, 'URL': p_source})
                try:
                    nextbtn = driver.find_element(By.CLASS_NAME, 'pagination-next')
                    nextbtn.click()
                except Exception as e:
                    # print(e)
                    next_found = False
        # print(product_list)
        return product_list
    except Exception as e:
        return list()

def write_csv(rows,filename):
    # fields = ['Product Name', 'Price', 'Size', 'Status']
    rows = rows

    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        # csvwriter.writerow(fields)
        csvwriter.writerows(rows)
    print("[INFO] File write successfull.")

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
        driver.maximize_window()

    try:
        filename = "product_details.csv"

        ## call function        
        url = 'https://www.backontrack-uk.co.uk/'

        ## For all the urls
        productList = getAllproductLink(driver,url)
        for product_url in productList:
            detailList = product_details(driver,product_url)
            print(detailList,'  ---   ---- --- ')
            write_csv(detailList,filename)


        ## for single url
        # productUrl = "https://www.backontrack-uk.co.uk/ourshop/prod_5310380-Back-on-Track-Canine-Fleece-RugSupreme.html"
        # detailList = product_details(driver,productUrl)
        # filename = "product_details.csv"
        # write_csv(detailList,filename)

    except Exception as e:
        print(e)    


if __name__ == "__main__":
    main()

