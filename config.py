# coding=utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = '12345'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/decision_support'