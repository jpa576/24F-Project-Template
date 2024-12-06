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

@Assessments.route('/save_submission', methods=['POST'])
def save_submission():
    try:
        # Get JSON payload from the request
        data = request.get_json()

        # Validate input
        required_fields = ['user_id', 'assessment_id', 'career_path_id', 'submitted_code', 'execution_result', 'status']
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            current_app.logger.error(f"Missing fields in request: {missing_fields}")
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        # Input validation
        if not isinstance(data['user_id'], int) or not isinstance(data['assessment_id'], int) or not isinstance(data['career_path_id'], int):
            return jsonify({"error": "Invalid ID type. Must be integers."}), 400
        if not isinstance(data['submitted_code'], str) or not isinstance(data['execution_result'], str):
            return jsonify({"error": "Invalid type for submitted_code or execution_result. Must be strings."}), 400
        if data['status'] not in ['correct', 'incorrect']:
            return jsonify({"error": "Invalid status. Must be 'correct' or 'incorrect'."}), 400

        # Insert submission into the database
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO UserCodingSubmissions 
                (user_id, assessment_id, career_path_id, submitted_code, execution_result, status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                data['user_id'],
                data['assessment_id'],
                data['career_path_id'],
                data['submitted_code'],
                data['execution_result'],
                data['status']
            ))
            connection.commit()

        return jsonify({"message": "Submission saved successfully!"}), 201

    except Exception as e:
        current_app.logger.error(f"Error saving coding submission: {e}")
        return jsonify({"error": "An error occurred while saving the submission."}), 500


@Assessments.route('/career_assessments/<int:career_path_id>', methods=['GET'])
def get_career_assessments(career_path_id):
    try:
        print(f"Route accessed with career_path_id: {career_path_id}")  # Debug statement
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
                SELECT ca.assessment_id, ca.problem_statement, ca.input_example, ca.expected_output
                FROM CareerPathAssessments cpa
                JOIN CodingAssessments ca ON cpa.assessment_id = ca.assessment_id
                WHERE cpa.career_path_id = %s
            """, (career_path_id,))
            data = cursor.fetchall()
        return jsonify({"status": "success", "data": data or []}), 200
    except Exception as e:
        print(f"Error in route: {e}")  # Debug statement
        current_app.logger.error(f"Error fetching assessments for career path {career_path_id}: {e}")
        return jsonify({"error": "An error occurred while fetching assessments."}), 500
