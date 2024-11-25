########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of
# routes.
Courses = Blueprint('courses', __name__)


## Get all academic courses from the system
@Courses.route('/courses', methods=['GET'])
def get_courses():
    try:
        # Get a cursor object from the database connection
        cursor = db.get_db().cursor()

        # Query to fetch all academic courses
        cursor.execute('''
            SELECT department, course_number, course_name, course_description, credits
            FROM AcademicCourses
        ''')

        # Fetch all the rows from the result
        the_data = cursor.fetchall()

        # Create the response with the fetched data
        the_response = make_response(jsonify(the_data))
        the_response.status_code = 200
        return the_response

    except Exception as e:
        # Return an error response in case of failure
        return make_response(jsonify({"error": str(e)}), 500)

    finally:
        # Ensure the cursor is closed after the operation
        cursor.close()
