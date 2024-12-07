from flask import Blueprint, request, jsonify, current_app, g
import pymysql
import os

courses = Blueprint('courses', __name__)

def get_db_connection():
    if 'db' not in g:
        g.db = pymysql.connect(
            host=os.getenv('MYSQL_HOST', 'localhost'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', ''),
            database=os.getenv('MYSQL_DATABASE', ''),
            port=int(os.getenv('MYSQL_PORT', 3306))
        )
    return g.db

@courses.teardown_app_request
def close_db_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@courses.route('/all_courses', methods=['GET'])
def get_all_courses():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM AcademicCourses")
            data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        current_app.logger.error(f"Error fetching all courses: {e}")
        return jsonify({"error": "An error occurred while fetching courses."}), 500

@courses.route('/concentration_courses', methods=['GET'])
def get_concentration_courses():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
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
        current_app.logger.error(f"Error fetching concentration courses: {e}")
        return jsonify({"error": "An error occurred while fetching concentration courses."}), 500

@courses.route('/courses_without_skills', methods=['GET'])
def get_courses_without_skills():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT ac.department, ac.course_number, ac.course_name
                FROM AcademicCourses ac
                LEFT JOIN CourseTechSkills cts
                    ON ac.department = cts.department
                    AND ac.course_number = cts.course_number
                WHERE cts.tech_skill_id IS NULL;
            """)
            data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        current_app.logger.error(f"Error fetching courses without skills: {e}")
        return jsonify({"error": "An error occurred while fetching courses without skills."}), 500

@courses.route('/add_course', methods=['POST'])
def add_course():
    try:
        # Parse JSON data from the request
        data = request.get_json()
        department = data.get("department")
        course_number = data.get("course_number")
        course_name = data.get("course_name")
        description = data.get("description")
        credits = data.get("credits")

        # Validate required fields
        if not all([department, course_number, course_name, credits]):
            return jsonify({"error": "Missing required fields (department, course_number, course_name, credits)."}), 400

        connection = get_db_connection()
        with connection.cursor() as cursor:
            # Check for duplicate entries
            cursor.execute("""
                SELECT COUNT(*) FROM AcademicCourses
                WHERE department = %s AND course_number = %s
            """, (department, course_number))
            if cursor.fetchone()[0] > 0:
                return jsonify({"error": "Course with the same department and course number already exists."}), 400

            # Insert new course
            cursor.execute("""
                INSERT INTO AcademicCourses (department, course_number, course_name, course_description, credits)
                VALUES (%s, %s, %s, %s, %s)
            """, (department, course_number, course_name, description, credits))
            connection.commit()

        return jsonify({"message": "Course added successfully!"}), 201
    except pymysql.MySQLError as db_err:
        current_app.logger.error(f"MySQL Error: {db_err}")
        return jsonify({"error": f"Database error: {db_err}"}), 500
    except Exception as e:
        current_app.logger.error(f"Unexpected error: {e}")
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500
