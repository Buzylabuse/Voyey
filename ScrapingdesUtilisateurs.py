#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 17:36:58 2021

@author: victorbuzy
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import shutil




Path = '/Users/victorbuzy/Desktop/projetpython/chromedriver'
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1200x600') # optional
driver = webdriver.Chrome(Path)
driver.get("https://admin.voyey.com/")
time.sleep(1)

search = driver.find_element_by_css_selector('#user-login > div:nth-child(2) > input')
search.send_keys("victor@voyey.com")
search.send_keys(Keys.RETURN)
time.sleep(1)
search = driver.find_element_by_css_selector('#user-login > div:nth-child(3) > input')
search.send_keys("V1ctor123@")
search.send_keys(Keys.RETURN)
time.sleep(1)



python_button = driver.find_element_by_css_selector('#main-wrapper > div > div:nth-child(35) > div > a')
python_button.click()

python_button = driver.find_element_by_css_selector('#users-list_wrapper > div.dt-buttons > button.dt-button.export-csv.export-data')
python_button.click()

time.sleep(5)
os.rename('/Users/victorbuzy/Downloads/users.csv', '/Users/victorbuzy/Downloads/UtilisateursVoyey.csv')

filePath = shutil.copy('/Users/victorbuzy/Downloads/UtilisateursVoyey.csv', '/Users/victorbuzy/Desktop/projetpython/Voyeyproject/Modules/')

driver.close()
driver.quit()


