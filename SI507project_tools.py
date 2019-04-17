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
    # print ("getting data")
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

count = 0
pres_info_list = []
# iterate through list of crawl_links
for link in crawl_links:
    pres_dict = {}
    if count >= 45:
        break
    else:
        # get scraped data from cache or get request to site
        crawl_page = scrape_function(link)
        # make BeautifulSoup object from page
        crawl_soup = BeautifulSoup(crawl_page, features="lxml")
        #get the FUll Name of a pres and add to pres dict
        pres_name = crawl_soup.find("h2", {"class": "president-name"}).text
        pres_dict['pres_full_name'] = pres_name
        # target pres. facts wrapper element
        facts_wrapper = crawl_soup.find("div", {"class": "fast-facts-wrapper"})
        # iterate over all the divs in the class 'data'
        for div in facts_wrapper.find_all('div', {'class': 'data'}):
            #get the label tag
            label_text = div.label.text
            #get the info in the label's sibiling div and slipt on newlines-- this makes a list of the info in the div
            pres_info = div.label.next_sibling.next_sibling.text.split('\n')
            #iterate through the div list and grab only the items with text and pass on newlines
            for item in pres_info:
                if len(item) == 0:
                    pass
                else:
                    pres_dict[label_text] = item
        pres_info_list.append(pres_dict)
    count +=1
header = ['President Number', 'Last Name', 'First Name', 'Birthday', 'Education' 'Inagural Date', 'Religon', 'Career', 'Party']

#write a CSV file with president data-- if data not present write 'N/A'
with open("example_csv_table.csv", "w", newline="") as example_fh:
    writer = csv.writer(example_fh)
    writer.writerow(header)
    for pres_dic in pres_info_list:
        pn = pres_dic['President Number']
        name = pres_dic['pres_full_name']
        full_name = name.split()
        ln = full_name[-1]
        fn = full_name[0]
        bd = pres_dic['Birth Date']
        id = pres_dic['Inauguration Date']
        try:
            ed = pres_dic['Education']
        except:
            ed = 'N/A'
        rel = pres_dic['Religion']
        car = pres_dic['Career']
        par = pres_dic['Political Party']
        row = [pn, ln, fn, bd, ed, id, rel, car, par]
        writer.writerow(row)
