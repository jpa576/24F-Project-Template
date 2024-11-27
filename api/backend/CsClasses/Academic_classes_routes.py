########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint
from flask import request, jsonify, make_response, current_app
from backend.db_connection import db
from flask import Blueprint, jsonify
import pymysql
import os

courses = Blueprint('courses', __name__)



#------------------------------------------------------------

@courses.route('/data', methods=['GET'])
def get_data():
    connection = None
    cursor = None
    try:
        connection = pymysql.connect(
            host=os.getenv('MYSQL_HOST', 'localhost'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', ''),
            database=os.getenv('MYSQL_DATABASE', ''),
            port=int(os.getenv('MYSQL_PORT', 3306))
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM AcademicCourses")
        data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()



@courses.route('/data2', methods=['GET'])
def get_required_courses():
    connection = None
    cursor = None
    try:
        connection = pymysql.connect(
            host=os.getenv('MYSQL_HOST', 'localhost'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', ''),
            database=os.getenv('MYSQL_DATABASE', ''),
            port=int(os.getenv('MYSQL_PORT', 3306))
        )
        cursor = connection.cursor()
        cursor.execute("""SELECT
    ac.concentration_name,
    cc.department,
    cc.course_number,
    acs.course_name
FROM
    ConcentrationCourses cc
    INNER JOIN AcademicConcentrations ac ON cc.concentration_id = ac.concentration_id
    INNER JOIN AcademicCourses acs ON cc.department = acs.department AND cc.course_number = acs.course_number
ORDER BY
    ac.concentration_name,
    cc.department,
    cc.course_number;
""")
        data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
