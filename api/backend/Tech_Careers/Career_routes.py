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
            cursor.execute("SELECT * FROM CareerPaths")
            data = cursor.fetchall()
        return jsonify({"status": "success", "data": data}), 200
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
        return jsonify({"status": "success", "data": data or []}), 200
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
        return jsonify({"status": "success", "data": data}), 200
    except Exception as e:
        current_app.logger.error(f"Error fetching careers without skills: {e}")
        return jsonify({"error": "An error occurred while fetching careers without skills."}), 500

# Route to get careers ranked by salary
@careers.route('/by_salary', methods=['GET'])
def get_careers_by_salary():
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
                SELECT career_name, description, salary, demand
                FROM CareerPaths
                ORDER BY salary DESC
            """)
            data = cursor.fetchall()
        return jsonify({"status": "success", "data": data}), 200
    except Exception as e:
        current_app.logger.error(f"Error fetching careers by salary: {e}")
        return jsonify({"error": "An error occurred while fetching careers by salary."}), 500

# Route to update career progress for a user
@careers.route('/<int:user_id>/update_progress/<int:career_path_id>', methods=['PUT'])
def update_career_progress(user_id, career_path_id):
    try:
        # Parse the request data
        data = request.json
        progress_percentage = data.get("progress_percentage")

        if progress_percentage is None or not (0 <= progress_percentage <= 100):
            return jsonify({"error": "Invalid progress percentage. Must be between 0 and 100."}), 400

        connection = get_db_connection()
        with connection.cursor() as cursor:
            # Update the progress in the database
            cursor.execute("""
                UPDATE UserCareerProgress
                SET progress_percentage = %s
                WHERE user_id = %s AND career_path_id = %s
            """, (progress_percentage, user_id, career_path_id))
            connection.commit()

        return jsonify({"status": "success", "message": "Career progress updated successfully."}), 200
    except Exception as e:
        current_app.logger.error(f"Error updating career progress: {e}")
        return jsonify({"error": "An error occurred while updating career progress."}), 500

@careers.route('/add_career', methods=['POST'])
def add_career():
    """
    Add a new career to the CareerPaths table.
    """
    try:
        # Parse the request JSON
        data = request.get_json()
        career_name = data.get("career_name")
        description = data.get("description")
        salary = data.get("salary")
        demand = data.get("demand")

        # Validate required fields
        if not all([career_name, description, salary, demand]):
            return jsonify({"error": "Missing required fields."}), 400

        # Validate salary and demand inputs
        if not isinstance(salary, (int, float)) or salary < 0:
            return jsonify({"error": "Invalid salary. Must be a non-negative number."}), 400
        if not isinstance(demand, (int, float)) or not (1 <= demand <= 5):
            return jsonify({"error": "Invalid demand. Must be a number between 1 and 5."}), 400

        connection = get_db_connection()
        with connection.cursor() as cursor:
            # Insert the new career into the database
            cursor.execute("""
                INSERT INTO CareerPaths (career_name, description, salary, demand)
                VALUES (%s, %s, %s, %s)
            """, (career_name, description, salary, demand))
            connection.commit()

        return jsonify({"status": "success", "message": "Career added successfully!"}), 201
    except pymysql.MySQLError as db_err:
        current_app.logger.error(f"MySQL Error: {db_err}")
        return jsonify({"error": f"Database error: {db_err}"}), 500
    except Exception as e:
        current_app.logger.error(f"Unexpected error: {e}")
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500
