from flask import Blueprint, request, jsonify, current_app, g
import pymysql
import os

# Define Blueprint
careers = Blueprint('careers', __name__)

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
@careers.teardown_app_request
def close_db_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Route to get all career paths
@careers.route('/all_careers', methods=['GET'])
def get_all_careers():
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
                SELECT *
                FROM CareerPaths
            """)
            data = cursor.fetchall()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        current_app.logger.error(f"Error fetching all careers: {e}")
        return jsonify({"error": "An error occurred while fetching careers."}), 500

# Route to get skills for a specific career path
@careers.route('/career_skills', methods=['GET'])
def get_career_skills():
    career_path_id = request.args.get('career_path_id')
    if not career_path_id:
        return jsonify({"error": "Missing 'career_path_id' parameter"}), 400
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
                SELECT ts.skill_name, ts.complexity, cks.relevance
                FROM CareerPathSkills cks
                JOIN TechSkills ts ON cks.tech_skill_id = ts.tech_skill_id
                WHERE cks.career_path_id = %s
            """, (career_path_id,))
            data = cursor.fetchall()
        return jsonify({"status": "success", "data": data or []})
    except Exception as e:
        current_app.logger.error(f"Error fetching career skills: {e}")
        return jsonify({"error": "An error occurred while fetching career skills."}), 500

# Route to get careers without skills
@careers.route('/career_skills2', methods=['GET'])
def get_career_noskills():
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
                SELECT DISTINCT cp.career_name
                FROM CareerPaths cp
                LEFT JOIN CareerPathSkills cks ON cp.career_path_id = cks.career_path_id
                WHERE cks.tech_skill_id IS NULL
            """)
            data = cursor.fetchall()
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        current_app.logger.error(f"Error fetching careers without skills: {e}")
        return jsonify({"error": "An error occurred while fetching careers without skills."}), 500
