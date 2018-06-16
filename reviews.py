# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup as soup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#adding incognito
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

#opening an instance of browser
driver = webdriver.Chrome(executable_path='/Users/aayushsharma/python/voterlist/chromedriver',chrome_options=option)
driver.get("http://www.educatenepal.com/college_review/all_reviews")
review={}
invoker = driver.execute_script('update_search(11,0);')
# element = WebDriverWait(driver,40).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"search_result_title")))
# page_html = driver.page_source