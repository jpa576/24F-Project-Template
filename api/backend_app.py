###
# Main application interface
###

from flask import Flask, jsonify, request
import mysql.connector
app = Flask(__name__)


# import the create app function 
# that lives in src/__init__.py
from backend.rest_entry import create_app

# create the app object
app = create_app()


# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",  # Replace with your MySQL host
        user="your_user",  # Replace with your MySQL username
        password="your_password",  # Replace with your MySQL password
        database="algonauts_db"  # Replace with your database name
    )

# Route for fetching skills
@app.route('/api/skills/<user_id>', methods=['GET'])
def get_skills(user_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT skill_name, progress 
        FROM UserSkills 
        WHERE user_id = %s
    """
    cursor.execute(query, (user_id,))
    skills = cursor.fetchall()
    connection.close()
    return jsonify(skills)

# Route for fetching courses
@app.route('/api/courses/<user_id>', methods=['GET'])
def get_courses(user_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT course_name, status 
        FROM UserCourses 
        WHERE user_id = %s
    """
    cursor.execute(query, (user_id,))
    courses = cursor.fetchall()
    connection.close()
    return jsonify(courses)

if __name__ == '__main__':
    # we want to run in debug mode (for hot reloading) 
    # this app will be bound to port 4000. 
    # Take a look at the docker-compose.yml to see 
    # what port this might be mapped to... 
    app.run(debug = True, host = '0.0.0.0', port = 4000)

