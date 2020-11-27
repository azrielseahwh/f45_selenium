import os
import os.path
import platform
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import time

def book_first_class():
    classes = driver.find_element_by_id('tabA7')
    classes.click()
    day_toggle = driver.find_element_by_id('day-tog-c')
    day_toggle.click()
    next_week_date = driver.find_element_by_id('week-arrow-r')
    next_week_date.click()
    try:
        rows = driver.find_element_by_class_name('classSchedule-mainTable-loaded').find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
        j = rows[1].find_elements_by_tag_name('td')[1].find_element_by_tag_name('input')
        j.click()
        time.sleep(3)
        submit = driver.find_element_by_name('SubmitEnroll2')
        submit.click()
        print("Successfully booked first class!!")
    except:
        print("Slot is already booked!!")
        
def book_second_class():
    classes = driver.find_element_by_id('tabA7')
    classes.click()
    day_toggle = driver.find_element_by_id('day-tog-c')
    day_toggle.click()
    next_week_date = driver.find_element_by_id('week-arrow-r')
    next_week_date.click()
    try:
        rows = driver.find_element_by_class_name('classSchedule-mainTable-loaded').find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
        j = rows[2].find_elements_by_tag_name('td')[1].find_element_by_tag_name('input')
        j.click()
        time.sleep(1)
        submit = driver.find_element_by_name('SubmitEnroll2')
        submit.click()
        print("Successfully booked second class!!")
    except:
        print("Slot is already booked!!")

if platform.system() == 'Windows':
    driver_file = 'chromedriver.exe'
else:
    driver_file = 'chromedriver'

t = time.localtime()
time_now = time.strftime("%H:%M:%S", t)

while time_now != "00:00:00":
    time.sleep(1)
    t = time.localtime()
    time_now = time.strftime("%H:%M:%S", t)
    print(time_now)
    if time_now == "23:59:30":
        driver_path = os.path.join(os.getcwd(), driver_file)
        driver = webdriver.Chrome(driver_path)
        link = "https://clients.mindbodyonline.com/ASP/main_shop.asp?studioid=494428&tg=22&vt=&lvl=&stype=41&view=&trn=0&page=&catid=&prodid=&date=9%2f28%2f2020&classid=0&prodGroupId=&sSU=&optForwardingLink=&qParam=&justloggedin=&nLgIn=&pMode=1&loc=1"
        driver.get(link)
        time.sleep(2)
        username = driver.find_element_by_id('su1UserName')
        username.send_keys('')
        password = driver.find_element_by_id('su1Password')
        password.send_keys('', Keys.RETURN)
    if time_now == "00:00:00":
        break

book_first_class()

driver.execute_script("window.open('{}');".format(link))
window_after = driver.window_handles[1]
driver.switch_to.window(window_after)
book_second_class()