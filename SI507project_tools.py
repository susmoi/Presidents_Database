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
    data = PROGRAM_CACHE.get_data(some_url)
    if not data:
        print("MAKING NEW REQUEST")
        data = requests.get(some_url).text
        PROGRAM_CACHE.set(some_url, data)
    return data

# scrape main page and turn data into BeautifulSoup object
main_page = scrape_function(START_URL)
soup = BeautifulSoup(main_page, features="html.parser")

# find_all a tag data from table on main page
pres_table = soup.find(id="block-mainpagecontent")
a_tags_list = soup.find_all('a', href=True)[3:47]

# create crawl links using main mage URL and a tag href_values
crawl_links = []
for a_tag in a_tags_list:
    href_value = a_tag["href"]
    link = f'https://millercenter.org{href_value}'
    crawl_links.append(link)

print (crawl_links)

#
# with open("example_csv_table.csv", "w", newline="") as example_fh:
#     writer = csv.writer(example_fh)
#     for row_tag in pres_table:
#         row_csv = row_tag.text.split()
#         writer.writerow(row_csv)
