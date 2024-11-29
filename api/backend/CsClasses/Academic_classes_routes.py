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

@courses.route('/course_info', methods=['GET'])
def course_info():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    ac.department AS course_department,
                    ac.course_number AS course_number,
                    ac.course_name AS course_name,
                    cp.prerequisite_department AS prereq_department,
                    cp.prerequisite_number AS prereq_number,
                    ac_prereq.course_name AS prereq_name,
                    cc.concentration_name AS concentration
                FROM
                    AcademicCourses ac
                LEFT JOIN
                    CoursePrerequisites cp
                    ON ac.department = cp.department AND ac.course_number = cp.course_number
                LEFT JOIN
                    AcademicCourses ac_prereq
                    ON cp.prerequisite_department = ac_prereq.department AND cp.prerequisite_number = ac_prereq.course_number
                LEFT JOIN
                    ConcentrationCourses cc
                    ON ac.department = cc.department AND ac.course_number = cc.course_number
                ORDER BY
                    cc.concentration_name, ac.department, ac.course_number;
            """)
            data = cursor.fetchall()
            return jsonify(data)
    except Exception as e:
            current_app.logger.error(f"Error fetching courses info: {e}")
            return jsonify({"error": "An error occurred while fetching course info."}), 500
