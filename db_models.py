import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy
from db import db


# Set up association Table between pres, ed, and religion
collections = db.Table('collections',
    db.Column("president_id", db.Integer, db.ForeignKey("presidents.id")),
    db.Column("education_id", db.Integer, db.ForeignKey("education.id")),
    db.Column("religion_id", db.Integer, db.ForeignKey("religion.id")))

class Education(db.Model):
    __tablename__ = "education"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))

    def __init__(self, ed_item):
        # self.id = educ_dic[ed_item]
        self.name = ed_item

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class Religon(db.Model):
    __tablename__ = "religion"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(600))

    def __init__(self, rel_item):
        self.name = rel_item

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

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

    education_id = db.Column(db.Integer, db.ForeignKey("education.id"))
    religion_id = db.Column(db.Integer,db.ForeignKey("religion.id"))
    #
    education = db.relationship("Education", backref="President")
    religon = db.relationship("Religon", backref="President")

    def __init__(self, pres_class, educ_dic, reli_dic):
        # self.id = id
        self.pres_num = pres_class.pn
        self.last_name = pres_class.ln
        self.first_name = pres_class.fn
        self.birthday = pres_class.bd
        self.education_id = educ_dic[pres_class.ed]
        self.inagural_day = pres_class.id
        self.religion_id = reli_dic[pres_class.rel]
        self.career = pres_class.car
        self.party = pres_class.par

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()



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
