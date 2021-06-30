from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, Text, DateTime, Boolean
from sqlalchemy import ForeignKey, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

from flaskr.app import db


# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     login = db.Column(db.String(100), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
#
#     def __repr__(self):
#         return '<User %r>' % self.login
#
#
# class Account(db.Model):
#     __tablename__ = 'accounts'
#     id = db.Column(db.Integer, primary_key=True)
#     balance = db.Column(db.Integer, nullable=False)
#
#     def __repr__(self):
#         return '<Account %r>' % self.balance
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     print('user')
#
#     def __repr__(self):
#         return '<User %r>' % self.username
