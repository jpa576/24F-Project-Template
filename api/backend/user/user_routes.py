from flask import Blueprint, request, jsonify, current_app, g
import pymysql
import os

# Define Blueprint
user = Blueprint('user', __name__)

# Database connection setup
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

# Close DB connection after each request
@user.teardown_app_request
def close_db_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Route to get user info by user_id
@user.route('/user/<int:user_id>/info', methods=['GET'])
def get_user_info(user_id):
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM Users WHERE user_id = %s", (user_id,))
            data = cursor.fetchone()
        if not data:
            return jsonify({"error": "User not found."}), 404
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        current_app.logger.error(f"Error fetching user info: {e}")
        return jsonify({"error": "An error occurred while fetching user info."}), 500

# Route to get user skills by user_id
@user.route('/user/<int:user_id>/skills', methods=['GET'])
def get_user_skills(user_id):
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
                SELECT us.user_skill_id, ts.skill_name, us.acquired_date 
                FROM UserSkills us
                JOIN TechSkills ts ON us.tech_skill_id = ts.tech_skill_id
                WHERE us.user_id = %s
            """, (user_id,))
            data = cursor.fetchall()
        return jsonify({"status": "success", "data": data or []})
    except Exception as e:
        current_app.logger.error(f"Error fetching user skills: {e}")
        return jsonify({"error": "An error occurred while fetching user skills."}), 500

# Route to get user career progress by user_id
@user.route('/user/<int:user_id>/progress', methods=['GET'])
def get_user_progress(user_id):
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
                SELECT 
                    c.career_name, 
                    ucp.progress_percentage
                FROM 
                    UserCareerProgress ucp
                JOIN 
                    CareerPaths c ON ucp.career_path_id = c.career_path_id
                WHERE 
                    ucp.user_id = %s
            """, (user_id,))
            data = cursor.fetchall()
        return jsonify({"status": "success", "data": data or []})
    except Exception as e:
        current_app.logger.error(f"Error fetching user progress: {e}")
        return jsonify({"error": "An error occurred while fetching user progress."}), 500

# Route to get user careers by user_id
@user.route('/user/<int:user_id>/careers', methods=['GET'])
def get_user_careers(user_id):
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
                SELECT DISTINCT 
                    c.career_name
                FROM 
                    UserCareerProgress ucp
                JOIN 
                    CareerPaths c ON ucp.career_path_id = c.career_path_id
                WHERE 
                    ucp.user_id = %s
            """, (user_id,))
            data = cursor.fetchall()
        return jsonify({"status": "success", "data": data or []})
    except Exception as e:
        current_app.logger.error(f"Error fetching user careers: {e}")
        return jsonify({"error": "An error occurred while fetching user careers."}), 500
