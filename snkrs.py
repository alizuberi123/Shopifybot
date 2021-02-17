from selenium import webdriver
from selenium.webdriver import ActionChains
import time
##from selenium.webdriver.common.keys import keys
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#ENTER URL TO PRODUCT
driver.get("https://www.deadstock.ca/products/comme-des-garcons-play-converse-chuck-taylor-hi-black?variant=31706207912021")
driver.maximize_window()



element1 = driver.find_element_by_id("ProductSelect-option-US Men's Size-11")
#element1 = driver.find_element_by_xpath('/html/body/div[5]/main/div/div/div[3]/div/div/div[2]/div[1]/div[1]/form/div[1]/div/label/fieldset/label[6]')
element1.click()
time.sleep(2)
element2 = driver.find_element_by_xpath('/html/body/div[5]/main/div/div/div[3]/div/div/div[2]/div/div[1]/form/div[2]/button')
element2.click()
time.sleep(2)
element3 = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/form/div[2]/a')
print("Hi!")
element3.click()
time.sleep(2)
element4 = driver.find_element_by_xpath('/html/body/div[5]/main/div/div/div/form/div[3]/div/div[2]/button[3]')
print("Hi")
element4.click()
time.sleep(2)
email = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/div[1]/div[2]/div[1]/div/div/input')
email.send_keys("ENTER EMAIL")
first_name = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/div[2]/div[2]/div/div/div[1]/div/input")
first_name.send_keys("ENTER FIRST NAME")
last_name = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/div[2]/div[2]/div/div/div[2]/div/input')
last_name.send_keys("ENTER LAST NAME")
address = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/div[2]/div[2]/div/div/div[4]/div/input')
address.send_keys("ENTER ADDRESS")
city = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/div[2]/div[2]/div/div/div[6]/div/input")
city.send_keys("ENTER STREET")
postalcode = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/div[2]/div[2]/div/div/div[9]/div/input')
postalcode.send_keys("ENTER POSTAL CODE")
phone = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[1]/form/div[1]/div[2]/div[2]/div/div/div[10]/div/input')
phone.send_keys('ENTER PHONE NUMBER')
element5 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/button')
element5.click()
time.sleep(2)
element6 = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[2]/div[1]/form/div[2]/button")
element6.click()
    #password1.send_keys(password)
    ##element23 = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/form/div[6]/input')
    #element23.click()
