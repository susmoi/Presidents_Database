import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from db import db
from SI507project_tools import *

# Application configurations
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./presidents_database_sample.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.secret_key = 'adgsdfsadfdflsdfsj'

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
    populate_data_into_db(list_of_class_pres)

@app.route('/')
def homepage():
    return render_template('home-route.html',list_of_class_pres=list_of_class_pres)

@app.route('/table')
def table():
    return render_template('table.html', list_of_class_pres=list_of_class_pres)

@app.route('/search/<fname>/<lname>')
def search(fname, lname):
    return render_template('search.html',fname=fname,lname=lname, list_of_class_pres=list_of_class_pres)

@app.route("/religion")
def religion_table():
    return render_template('religion.html', rel_dict=rel_dict)

@app.route("/education")
def education_table():
    return render_template('education.html', ed_dict=ed_dict)


if __name__ == '__main__':
    app.run(port=5000, debug=True) # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
#
# session = db.session # to make queries easy
