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

@tech_skills.route('/add_skill', methods=['POST'])
def add_skill():
    """
    Add a new skill to the TechSkills table.
    """
    try:
        # Parse request JSON
        data = request.get_json()
        skill_name = data.get("skill_name")
        complexity = data.get("complexity")
        description = data.get("description")
        popularity_score = data.get("popularity_score")

        # Validate inputs
        if not all([skill_name, complexity, description, popularity_score]):
            return jsonify({"error": "Missing required fields."}), 400

        connection = get_db_connection()
        with connection.cursor() as cursor:
            # Insert the new skill
            cursor.execute("""
                INSERT INTO TechSkills (skill_name, complexity, description, popularity_score)
                VALUES (%s, %s, %s, %s)
            """, (skill_name, complexity, description, popularity_score))
            connection.commit()

        return jsonify({"message": "Skill added successfully!"}), 201
    except pymysql.MySQLError as db_err:
        current_app.logger.error(f"MySQL Error: {db_err}")
        return jsonify({"error": f"Database error: {db_err}"}), 500
    except Exception as e:
        current_app.logger.error(f"Unexpected error: {e}")
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500
