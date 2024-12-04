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
@user.route('/<int:user_id>/info', methods=['GET'])
def get_user_info(user_id):
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT user_id, name, email, year, plan_id FROM Users WHERE user_id = %s", (user_id,))
            data = cursor.fetchone()
        if not data:
            return jsonify({"error": "User not found."}), 404
        return jsonify({"status": "success", "data": data})
    except Exception as e:
        current_app.logger.error(f"Error fetching user info: {e}")
        return jsonify({"error": "An error occurred while fetching user info."}), 500
