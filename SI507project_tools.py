import os
import requests
import json
from bs4 import BeautifulSoup
from advanced_expiry_caching import Cache
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
# from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this
from db import db
from db_models import President



#Constants
FNAME = "example_json_file.json"
START_URL = "https://millercenter.org/president"
CSV_FILE = "example_csv_table.csv"

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
pres_data_list = [] #list is a dict. Each dict-- Key is label text, Value is facts_wrapper_div text

# iterate through list of crawl_links and scrape president data from fact sheet and append data to list
for link in crawl_links:
    pres_dict = {}
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
    for facts_wrapper_div in facts_wrapper.find_all('div', {'class': 'data'}):
        #get the label tag TEXT and label tag sibling TEXT
        label_text = facts_wrapper_div.label.text #['President Number', 'Last Name', 'First Name', 'Birthday', 'Education' ,'Inaugural Date', 'Religion', 'Career', 'Party']
        pres_data_text_list = facts_wrapper_div.label.next_sibling.next_sibling.text.split('\n') #this makes a list of the info in the div

        #iterate through the pres_data list and seperate TEXT from \n (newlines)
        for text in pres_data_text_list:
            if len(text) == 0:
                pass
            else:
                pres_dict[label_text] = text #Key is label text, Value is facts_wrapper_div text

    pres_data_list.append(pres_dict)

class US_President:
    def __init__(self, list):
        self.pn = list[0]
        self.ln = list[1]
        self.fn = list[2]
        self.bd = list[3]
        self.ed = list[4]
        self.id = list[5]
        self.rel = list[6]
        self.car = list[7]
        self.par = list[8]

    def __str__(self):
        return f"{self.fn} {self.ln} was the number {self.pn} President of the United States of America and they represented the {self.par} party. They were born on {self.bd} and recieved an education from {self.ed}. Their career before becoming president was {self.car}. They were inaugurated on {self.id}. Their religion was/is {self.rel}."

list_of_class_pres = [] #Contains list of US_President objects

def make_pres_list(list_of_dicts):
    #['President Number', 'Last Name', 'First Name', 'Birthday', 'Education' ,'Inaugural Date', 'Religion', 'Career', 'Party']
    for single_dict in list_of_dicts:
        pn = single_dict['President Number']
        name = single_dict['pres_full_name']
        full_name = name.split()
        ln = full_name[-1]
        fn = full_name[0]
        bd = single_dict['Birth Date']
        id = single_dict['Inauguration Date']
        try:
            ed = single_dict['Education']
        except:
            ed = 'N/A'
        rel = single_dict['Religion']
        car = single_dict['Career']
        par = single_dict['Political Party']
        row = [pn, ln, fn, bd, ed, id, rel, car, par]
        pres = US_President(row) #pres is an instance of US_President Class
        list_of_class_pres.append(pres)
    return list_of_class_pres

make_pres_list(pres_data_list) #creates a list of US_President objects

def populate_data_into_db(list):
    for pres_list_item in list:
        new_pres = President(pres_class=pres_list_item, id=1)
        new_pres.save_to_db()
