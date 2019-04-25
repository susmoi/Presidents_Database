import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy
from db import db


# Set up association Table between pres, ed, and religion
# collections = db.Table('collections',
#     db.Column("president_id", db.Integer, db.ForeignKey("presidents.id")),
#     db.Column("education_id", db.Integer, db.ForeignKey("education.id")),
#     db.Column("religion_id", db.Integer, db.ForeignKey("religion.id")))

class President(db.Model):
    __tablename__ = "presidents"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pres_num = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    first_name = db.Column(db.String(64))
    birthday = db.Column(db.String(64))
    inagural_day = db.Column(db.String(64))
    career = db.Column(db.String(64))
    party = db.Column(db.String(64))
    # education_id = db.Column(db.Integer, db.ForeignKey("education.id"))
    # religion_id = db.Column(db.Integer,db.ForeignKey("religion.id"))

    def __init__(self, pres_class, id = None):
        self.pres_num = pres_class.pn
        self.last_name = pres_class.ln
        self.first_name = pres_class.fn
        self.birthday = pres_class.bd
        self.education = pres_class.ed
        self.inagural_day = pres_class.id
        self.religion = pres_class.rel
        self.career = pres_class.car
        self.party = pres_class.par


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


# class Education(db.Model):
#     __tablename__ = "education"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))
#
#
# class Religon(db.Model):
#     __tablename__ = "religion"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))
#
#     def __repr__(self):
#         return "{} (ID: {})".format(self.name,self.id)



#
# class Movie(db.Model):
#     __tablename__ = "movies"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(64), unique=True)
#     genre = db.Column(db.String(64), unique=True)
#     president_id = db.Column(db.Integer, db.ForeignKey("presidents.id"))
#
#     def __repr__(self):
#         return "{} by {} | {}".format(self.title,self.president_id, self.genre)
#
# def get_or_create_director(director_name):
#     president = President.query.filter_by(name=director_name).first()
#     if president:
#         return president
#     else:
#         president = President(name=director_name)
#         session.add(president)
#         session.commit()
#         return president
#
##
# csv_pres_rows = []
# with open (CSV_FILE, "r") as fh:
#     reader = csv.reader(fh)
#     for row in reader:
#         csv_pres_rows.append(row)
#
# HEADER = ['President Number', 'Last Name', 'First Name', 'Birthday', 'Education', 'Inagural Date', 'Religon', 'Career', 'Party']
# for item in csv_pres_rows:
#     # print (item[8])
#     # print (len(item))
#     pass
#
# class President():
#     '''A class which represents one US president'''
#     #assign each pres. info--such as-- name, birthday, education, etc.
#     def __init__(self, row_of_data):
#         for item in row_of_data:
#             self.pn = row_of_data[0]
#             self.ln = row_of_data[1]
#             self.fn = row_of_data[2]
#             self.bd = row_of_data[3]
#             self.ed = row_of_data[4]
#             self.id = row_of_data[5]
#             self.rel = row_of_data[6]
#             self.car = row_of_data[7]
#             self.par = row_of_data[8]
#
# def create_pres_obj(list_of_lists):
#     for list in list_of_lists:
#         president1 = President(row)
