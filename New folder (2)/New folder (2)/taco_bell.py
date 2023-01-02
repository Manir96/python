from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.ubereats.com/store/taco-bell-710-third-street/If7-LLLYTn-Ua90XcFZx1w?diningMode=DELIVERY&pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMlRoZSUyMFBpenphJTIwQm95JTIyJTJDJTIycmVmZXJlbmNlJTIyJTNBJTIyQ2hJSlc1Y29LZ2I3X1RrUnJWWm5BaWFVbTFBJTIyJTJDJTIycmVmZXJlbmNlVHlwZSUyMiUzQSUyMmdvb2dsZV9wbGFjZXMlMjIlMkMlMjJsYXRpdHVkZSUyMiUzQTI0LjI1ODA2NDclMkMlMjJsb25naXR1ZGUlMjIlM0E4OS45MTYzMzY1JTdE')

prod_title_list= []
product_price_list= []

prod_array = [12,13,11,4,10,7,12,3,2,8,2,19,15,2,18]
l = 0
row = 0
cat_dicts = {}
for i in range(1,16):
    temp_list = []
    temp_list_price = []
    for j in range(1,prod_array[l]+1): 
        prod_title = WebDriverWait(driver, 30).until(EC.
        presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[4]/div[2]/div[4]/ul/li['+str(i)+']/ul/li['+str(j)+']/div/div/div[2]/div[1]/div/span')))
        #prod_title = driver.find_element(by=By.XPATH, value = '//*[@id="main-content"]/div[4]/div/div[4]/ul/li['+str(i)+']/ul/li['+str(j)+']/div/div/div[2]/div[1]/div/span')
        prod_title_list.append(prod_title.text)
        prod_price = WebDriverWait(driver, 30).until(EC.
        presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div[4]/div[2]/div[4]/ul/li['+str(i)+']/ul/li['+str(j)+']/div/div/div[2]/div[2]/span')))
       # product_price = driver.find_element(by=By.XPATH, value = '//*[@id="main-content"]/div[4]/div[1]/div[4]/ul/li[1]/ul/li['+str(i)+']/div/div/div[2]/div[2]/span[1]')
        product_price_list.append(prod_price.text)
        temp_list.append(prod_title.text)
        temp_list_price.append(prod_price.text)
    cat_dicts[i-1] = [temp_list,temp_list_price]
    
    l = l+1
    
print(prod_title_list)
print(product_price_list)
print(len(prod_title_list)) 
print(cat_dicts)
time.sleep(50)