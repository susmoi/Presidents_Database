import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy
import csv
from SI507project_tools import *

# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy

#create db class definitions

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsdfsadfdflsdfsj'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./movies_database.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy

collections = db.Table('collections',db.Column('movie_id', db.Integer, db.ForeignKey("movies.id")), db.Column("director_id", db.Integer, db.ForeignKey("directors.id")))

class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return "{} (ID: {})".format(self.name,self.id)

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True)
    genre = db.Column(db.String(64), unique=True)
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"))

    def __repr__(self):
        return "{} by {} | {}".format(self.title,self.director_id, self.genre)

def get_or_create_director(director_name):
    director = Director.query.filter_by(name=director_name).first()
    if director:
        return director
    else:
        director = Director(name=director_name)
        session.add(director)
        session.commit()
        return director







csv_pres_rows = []
with open (CSV_FILE, "r") as fh:
    reader = csv.reader(fh)
    for row in reader:
        csv_pres_rows.append(row)

HEADER = ['President Number', 'Last Name', 'First Name', 'Birthday', 'Education', 'Inagural Date', 'Religon', 'Career', 'Party']
for item in csv_pres_rows:
    # print (item[8])
    # print (len(item))
    pass

class President():
    '''A class which represents one US president'''
    #assign each pres. info--such as-- name, birthday, education, etc.
    def __init__(self, row_of_data):
        for item in row_of_data:
            self.pn = row_of_data[0]
            self.ln = row_of_data[1]
            self.fn = row_of_data[2]
            self.bd = row_of_data[3]
            self.ed = row_of_data[4]
            self.id = row_of_data[5]
            self.rel = row_of_data[6]
            self.car = row_of_data[7]
            self.par = row_of_data[8]

def create_pres_obj(list_of_lists):
    for list in list_of_lists:
        president1 = President(row)
