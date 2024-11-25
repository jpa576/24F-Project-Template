########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint
from flask import request, jsonify, make_response, current_app
from backend.db_connection import db

#------------------------------------------------------------
from flask import Blueprint, jsonify
import pymysql
import os

courses = Blueprint('courses', __name__)

@courses.route('/debug', methods=['GET'])
def debug_connection():
    try:
        # Establish the database connection
        connection = pymysql.connect(
            host=os.getenv('MYSQL_HOST', 'localhost'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', ''),
            database=os.getenv('MYSQL_DATABASE', ''),  # Ensure this is set
            port=int(os.getenv('MYSQL_PORT', 3306))
        )
        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE();")  # Verify the selected database
        current_db = cursor.fetchone()
        return jsonify({"database": current_db[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()


#------------------------------------------------------------


courses = Blueprint('courses', __name__)

@courses.route('/courses', methods=['GET'])
def get_courses():
    try:
        # Get a database connection
        db = get_db()
        cursor = db.cursor()

        # Query to fetch all academic courses
        query = '''
            SELECT department,
                   course_number,
                   course_name,
                   course_description,
                   credits
            FROM AcademicCourses
        '''

        # Logging the query for debugging purposes
        current_app.logger.info(f'GET /courses query={query}')

        # Execute the query and fetch the results
        cursor.execute(query)
        courses_data = cursor.fetchall()

        # Logging the fetched data for debugging purposes
        current_app.logger.info(f'GET /courses Result of query = {courses_data}')

        # Prepare and return the response
        return jsonify(courses_data), 200
    except Exception as e:
        current_app.logger.error(f'Error fetching courses: {e}')
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()