#------------------------------------------------------------
# This file creates a shared DB connection resource
#------------------------------------------------------------
import pymysql
from flaskext.mysql import MySQL
from pymysql import cursors
import os


# the parameter instructs the connection to return data 
# as a dictionary object. 
db = MySQL(cursorclass=cursors.DictCursor)


