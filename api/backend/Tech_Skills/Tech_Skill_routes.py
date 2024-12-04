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
def get_all_skills():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT *
                            FROM TechSkills""")
            data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        current_app.logger.error(f"Error fetching all courses: {e}")
        return jsonify({"error": "An error occurred while fetching courses."}), 500

@tech_skills.route('/skills/by_demand', methods=['GET'])
def get_skills_by_demand():
    """
    Fetch skills ranked by popularity score in descending order.
    """
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT skill_name, complexity, description, popularity_score
                FROM TechSkills
                ORDER BY popularity_score DESC
            """)
            data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        current_app.logger.error(f"Error fetching skills by demand: {e}")
        return jsonify({"error": "An error occurred while fetching skills by demand."}), 500
