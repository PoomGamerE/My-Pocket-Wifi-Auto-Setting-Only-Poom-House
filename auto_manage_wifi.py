from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

'''from selenium.webdriver.remote import webelement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


import time
from bs4 import BeautifulSoup
import os
from datetime import datetime
from selenium.webdriver import ActionChains'''
    
browser = webdriver.Edge(executable_path = 'C:\\Users\\mcinl\\AppData\\Local\\Programs\\Python\\msedgedriver.exe')

#Login Section
browser.get("http://192.168.0.1/html/home.html")
loginbutton = browser.find_element_by_id("logout_span")
loginbutton.click()

try:
    username = browser.find_element_by_id("username")
    
    password = browser.find_element_by_id("password")
    loginbutton = browser.find_element_by_id("pop_login")

    username.send_keys("admin")
    password.send_keys("admin")
    loginbutton.click()
except:
    pass

'''
try:
    cancelbutton = browser.find_element_by_id("pop_Cancel")
    cancelbutton.click()
except:
    pass

try:
    message = driver.find_element_by_xpath("//*[@class='index_connection_status']").text
    print(message)
except:
    pass

setting_btn = browser.find_element_by_id("settings")
setting_btn.click()'''

#Setting Dial-Up Section

browser.get("http://192.168.0.1/html/mobileconnection.html")

try:
    browser.find_element_by_id("mobilenetwork_turnOn_button").click()
    delay(2000)
    browser.find_element_by_css_selector("input[type='radio'][value='1']").click()
    applybutton = browser.find_element_by_id("apply")
    applybutton.click()
    okbutton = browser.find_element_by_id("pop_confirm")
    okbutton.click()
except:
    pass
    
#WLAN Dial-Up Section

browser.get("http://192.168.0.1/html/wlanbasicsettings.html")

try:
    #browser.find_element_by_id("ssid1_wifiName").sendKeys("uE005");
    WIFIName = browser.find_element_by_id("ssid1_wifiName")
    WIFIName.send_keys("PGE_Studio1")
    browser.find_element_by_css_selector("input[type='input_select'][value='SHARE']").click()
    applybutton = browser.find_element_by_id("pop_confirm")
    applybutton.click()
except:
    pass