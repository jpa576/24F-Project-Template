from flask import Blueprint, request, jsonify, current_app, g
import pymysql
import os

tech_skills = Blueprint('tech_skills', __name__)

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

@tech_skills.teardown_app_request
def close_db_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@tech_skills.route('/all_skills', methods=['GET'])
def get_all_courses():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM TechSkills")
            data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        current_app.logger.error(f"Error fetching all courses: {e}")
        return jsonify({"error": "An error occurred while fetching courses."}), 500

@tech_skills.route('/career_skills', methods=['GET'])
def get_concentration_courses():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                  cp.career_name, ts.skill_name
                FROM
                    CareerPathSkills cps
                    join algonauts_db.CareerPaths cp on cp.career_path_id = cps.career_path_id
                    join algonauts_db.TechSkills ts on ts.tech_skill_id = cps.tech_skill_id
                    order by cp.career_name
                """)
            data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        current_app.logger.error(f"Error fetching concentration courses: {e}")
        return jsonify({"error": "An error occurred while fetching concentration courses."}), 500

