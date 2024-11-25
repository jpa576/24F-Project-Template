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


# Establish the database connection
connection = pymysql.connect(
    host=os.getenv('MYSQL_HOST', 'localhost'),
    user=os.getenv('MYSQL_USER', 'root'),
    password=os.getenv('MYSQL_PASSWORD', ''),
    database=os.getenv('MYSQL_DATABASE', ''),  # Ensure this is set
    port=int(os.getenv('MYSQL_PORT', 3306))
)
