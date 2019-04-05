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

main_page = scrape_function(START_URL)

soup = BeautifulSoup(main_page, features="html.parser")

pres_table = soup.find(id="block-mainpagecontent")
# print(pres_table)
a_tags_list = soup.find_all('a', href=True)
count = 0
for item in a_tags_list:
    if count == 47:
        break
    else:
        print ("Found the URL:", item['href'])
        count += 1
#
# with open("example_csv_table.csv", "w", newline="") as example_fh:
#     writer = csv.writer(example_fh)
#     for row_tag in pres_table:
#         row_csv = row_tag.text.split()
#         writer.writerow(row_csv)
