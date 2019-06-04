'''
 Copy this and create a new config.py
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = '' #make your own secret key
    SQLALCHEMY_DATABASE_URI = '' #set your database uri or connection
    SQLALCHEMY_TRACK_MODIFICATIONS = False
