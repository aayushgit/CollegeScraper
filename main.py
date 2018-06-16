# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup as soup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
# adding incognito
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# opening an instance of browser
driver = webdriver.Chrome(executable_path='/Users/aayushsharma/python/voterlist/chromedriver', chrome_options=option)
driver.get("http://www.educatenepal.com/institutions")

college_list = []
college = {}
course = {}
course_list = []

invoker = driver.execute_script('goAdvancedSearch(0,0);')
element = WebDriverWait(driver, 40).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "search_result_title")))
page_html = driver.page_source
page_soup = soup(page_html, 'lxml')
# print(page_soup)
for links in page_soup.findAll("div", {"class": "search_result_title"}):
    link = links.find("a", href=True)
    driver.get(link['href'])
    college['name'] = link.text
    driver.find_element_by_id('tab2').click()
    element = WebDriverWait(driver, 40).until(EC.presence_of_all_elements_located((By.ID, "courselist")))
    page_html = driver.page_source
    page_soup = soup(page_html, 'lxml')
    for link in page_soup.findAll("a", href=True):
        if re.match("http://www.educatenepal.com/course/detail/", link['href']):
            if re.match("[^view]", link.text):
                course['course_name'] = link.text
        if re.match("http://www.educatenepal.com/affiliation_body/detail", link['href']):
            if re.match("[^view]", link.text):
                course['course_affiliation'] = link.text
                course_list.append(course.copy())
    side = page_soup.find("div", {"class": "width-205"})
    address = page_soup.find("div", {"class": "text-align-center padding-top-5 text-align-center font-size-11 padding-left-5 padding-right-5"})
    college['address'] = address.text.split()[0]

    college['course'] = course_list
    college_list.append(college.copy())
print(college_list)
with open("data.json", "w") as write_file:
    json.dump(college, write_file)
