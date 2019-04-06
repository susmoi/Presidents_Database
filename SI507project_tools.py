import os
import requests
import csv
from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this

#Constants
FNAME = "example_json_file.json"
START_URL = "https://millercenter.org/president"

PROGRAM_CACHE = Cache(FNAME)
# Function which either gets data from cache or creates new get request, then returns data
def scrape_function(some_url):
    print ("getting data")
    data = PROGRAM_CACHE.get_data(some_url)
    if not data:
        print("MAKING NEW REQUEST")
        data = requests.get(some_url).text
        PROGRAM_CACHE.set(some_url, data)
    return data

# scrape main page and turn data into BeautifulSoup object
main_page = scrape_function(START_URL)
main_soup = BeautifulSoup(main_page, features="html.parser")

# find_all a tag data from table on main page
pres_table = main_soup.find(id="block-mainpagecontent")
a_tags_list = main_soup.find_all('a', href=True)[3:47]

# create crawl links using main mage URL and a tag href_values
crawl_links = []
for a_tag in a_tags_list:
    href_value = a_tag["href"]
    link = f'https://millercenter.org{href_value}'
    crawl_links.append(link)

# print (crawl_links)

count = 0
# iterate through list of crawl_links
for link in crawl_links:
    if count >= 1:
        break
    else:
        # get scraped data from cache or get request to site
        crawl_page = scrape_function(link)
        # make BeautifulSoup object from page
        crawl_soup = BeautifulSoup(crawl_page, features="lxml")
        # target pres. facts wrapper element
        facts_wrapper = crawl_soup.find("div", {"class": "fast-facts-wrapper"})
        # create list of the all the div_text in facts_wrapper
        div_text_list = facts_wrapper.find_all('div', text=True)
        # iterate through list and grab pres info
        for div_text in div_text_list:
            full_name = div_text_list[0].text.split()
            l_name = full_name[1]
            f_name = full_name[0]
            birth_place = div_text_list[1].text
            education = div_text_list[2].text
            religion = div_text_list[3].text
            career = div_text_list[4].text
            pres_number =  div_text_list[-2].text

        time_text_list = facts_wrapper.find_all("time")
        for time_text in time_text_list:
            birth_date = time_text_list[0].text
            inauguration_date = time_text_list[2].text
        # create row from pres info
        row = [pres_number, l_name, f_name, birth_date, birth_place, education, career, religion]
        # print (row)
    count +=1
#
# with open("example_csv_table.csv", "w", newline="") as example_fh:
#     writer = csv.writer(example_fh)
#     for row_tag in pres_table:
#         row_csv = row_tag.text.split()
#         writer.writerow(row_csv)
