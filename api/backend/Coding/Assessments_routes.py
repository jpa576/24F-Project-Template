from flask import Blueprint, request, jsonify, current_app, g
import pymysql
import os

Assessments = Blueprint('Assessments', __name__)

# Database connection helper
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

@Assessments.teardown_app_request
def close_db_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Route to fetch all coding assessments
@Assessments.route('/all_assessments', methods=['GET'])
def get_coding_assessments():
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
                SELECT 
                    assessment_id, 
                    problem_statement, 
                    input_example, 
                    expected_output 
                FROM CodingAssessments
            """)
            data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        current_app.logger.error(f"Error fetching coding assessments: {e}")
        return jsonify({"error": "An error occurred while fetching coding assessments."}), 500

# Route to save a coding submission
@Assessments.route('/save_submission', methods=['POST'])
def save_submission():
    try:
        # Get JSON payload from the request
        data = request.get_json()

        # Validate input
        required_fields = ['user_id', 'assessment_id', 'submitted_code', 'execution_result', 'status']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Insert submission into the database
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO UserCodingSubmissions 
                (user_id, assessment_id, submitted_code, execution_result, status)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                data['user_id'],
                data['assessment_id'],
                data['submitted_code'],
                data['execution_result'],
                data['status']
            ))
            connection.commit()
        return jsonify({"message": "Submission saved successfully!"}), 201
    except Exception as e:
        current_app.logger.error(f"Error saving coding submission: {e}")
        return jsonify({"error": "An error occurred while saving the submission."}), 500
