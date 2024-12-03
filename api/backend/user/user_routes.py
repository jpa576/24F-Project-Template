from flask import Blueprint, request, jsonify, current_app, g
import pymysql
import os

user = Blueprint('user', __name__)

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

@user.teardown_app_request
def close_db_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@user.route('/all_user_info', methods=['GET'])
def get_all_user_info():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT *
                            FROM Users """)
            data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        current_app.logger.error(f"Error fetching: {e}")
        return jsonify({"error": "An error occurred."}), 500


@user.route('/user_skills', methods=['GET'])
def user_skills():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT *
                            FROM UserSkills """)
            data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        current_app.logger.error(f"Error fetching: {e}")
        return jsonify({"error": "An error occurred."}), 500

@user.route('/get_progress', methods=['GET'])
def get_progress():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
    u.name AS user_name, 
    c.career_name, 
    ucp.progress_percentage
FROM 
    UserCareerProgress ucp
JOIN 
    Users u ON u.user_id = ucp.user_id
JOIN 
    CareerPaths c ON c.career_path_id = ucp.career_path_id;
 """)
            data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        current_app.logger.error(f"Error fetching: {e}")
        return jsonify({"error": "An error occurred."}), 500



