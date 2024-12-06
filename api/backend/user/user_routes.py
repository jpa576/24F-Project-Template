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

# Route to get user skills by user_id
@user.route('/<int:user_id>/skills', methods=['GET'])
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
@user.route('/<int:user_id>/progress', methods=['GET'])
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
@user.route('/<int:user_id>/careers', methods=['GET'])
def get_user_careers(user_id):
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("""
                SELECT
                    c.career_name, c.career_path_id
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


#route to update user career choice
@user.route('/<int:user_id>/update_careers/<int:career_id>', methods=['PUT'])
def update_user_career(user_id, career_id):
    try:
        data = request.json
        progress_percentage = data.get("progress_percentage", None)

        if progress_percentage is None:
            return jsonify({"error": "Missing 'progress_percentage' in request body"}), 400

        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE UserCareerProgress
                SET progress_percentage = %s
                WHERE user_id = %s AND career_path_id = %s
            """, (progress_percentage, user_id, career_id))
            connection.commit()

        return jsonify({"status": "success", "message": "Career progress updated successfully."})
    except Exception as e:
        current_app.logger.error(f"Error updating user career: {e}")
        return jsonify({"error": "An error occurred while updating user career."}), 500

@user.route('/all_users', methods=['GET'])
def get_all_users():
    """
    Fetch all users with their basic information.
    """
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT user_id, name, email, year, plan_id FROM Users")
            users = cursor.fetchall()
        return jsonify({"status": "success", "data": users})
    except Exception as e:
        current_app.logger.error(f"Error fetching all users: {e}")
        return jsonify({"error": "An error occurred while fetching user data."}), 500

@user.route('/add_user', methods=['POST'])
def add_user():
    """
    Add a new user to the database.
    """
    try:
        data = request.json
        name = data.get("name")
        email = data.get("email")
        year = data.get("year")
        plan_id = data.get("plan_id", None)

        if not all([name, email, year]):
            return jsonify({"error": "Missing required fields: name, email, or year."}), 400

        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Users (name, email, year, plan_id)
                VALUES (%s, %s, %s, %s)
            """, (name, email, year, plan_id))
            connection.commit()

        return jsonify({"status": "success", "message": "User added successfully."}), 201
    except Exception as e:
        current_app.logger.error(f"Error adding user: {e}")
        return jsonify({"error": "An error occurred while adding the user."}), 500


@user.route('/<int:user_id>/remove_user', methods=['DELETE'])
def remove_user(user_id):
    """
    Remove a user by their user_id.
    """
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            # Check if user exists
            cursor.execute("SELECT * FROM Users WHERE user_id = %s", (user_id,))
            user = cursor.fetchone()
            if not user:
                return jsonify({"error": "User not found."}), 404

            # Delete the user
            cursor.execute("DELETE FROM Users WHERE user_id = %s", (user_id,))
            connection.commit()

        return jsonify({"status": "success", "message": f"User with ID {user_id} removed successfully."}), 200
    except Exception as e:
        current_app.logger.error(f"Error in /remove_user: {e}")
        return jsonify({"error": "An error occurred while removing the user."}), 500


@user.route('/<int:user_id>/update_progress', methods=['PUT'])
def update_user_progress(user_id):
    """
    Update the progression of a user in their career path.
    """
    try:
        data = request.json
        progress_percentage = data.get("progress_percentage")
        if progress_percentage is None:
            return jsonify({"error": "Progress percentage is required"}), 400

        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE UserCareerProgress
                SET progress_percentage = %s
                WHERE user_id = %s
            """, (progress_percentage, user_id))
            connection.commit()

        return jsonify({"status": "success", "message": "User progress updated successfully."})
    except Exception as e:
        current_app.logger.error(f"Error updating user progress: {e}")
        return jsonify({"error": "An error occurred while updating user progress."}), 500



@user.route('/<int:user_id>/pop_career/<int:career_id>', methods=['DELETE'])
def delete_user_career(user_id, career_id):
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM UserCareerProgress
                WHERE user_id = %s AND career_path_id = %s
            """, (user_id, career_id))
            connection.commit()

        return jsonify({"status": "success", "message": "Career path deleted successfully."})
    except Exception as e:
        current_app.logger.error(f"Error deleting user career: {e}")
        return jsonify({"error": "An error occurred while deleting user career."}), 500

@user.route('/<int:user_id>/add_careers', methods=['POST'])
def add_user_career(user_id):
    try:
        data = request.json
        career_path_id = data.get("career_path_id")
        progress_percentage = data.get("progress_percentage", 0.00)  # Default progress is 0

        if not career_path_id:
            return jsonify({"error": "Missing 'career_path_id' in request body"}), 400

        connection = get_db_connection()
        with connection.cursor() as cursor:
            # Check if the career path already exists for the user
            cursor.execute("""
                SELECT * FROM UserCareerProgress
                WHERE user_id = %s AND career_path_id = %s
            """, (user_id, career_path_id))
            if cursor.fetchone():
                return jsonify({"error": "Career path already exists for the user."}), 400

            # Insert new career path for the user
            cursor.execute("""
                INSERT INTO UserCareerProgress (user_id, career_path_id, progress_percentage)
                VALUES (%s, %s, %s)
            """, (user_id, career_path_id, progress_percentage))
            connection.commit()

        return jsonify({"status": "success", "message": "Career path added successfully."}), 201
    except Exception as e:
        current_app.logger.error(f"Error adding career path: {e}")
        return jsonify({"error": "An error occurred while adding the career path."}), 500


@user.route('/<int:user_id>/academic_progress', methods=['GET'])
def get_academic_progress(user_id):
    """
    Fetch academic progression data for a user, including current (in-progress),
    completed, and required (not-started) courses.
    """
    try:
        connection = get_db_connection()
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            # Fetch current courses (in-progress)
            cursor.execute("""
                SELECT 
                    ucp.department AS Department, 
                    ucp.course_number AS `Course Number`,
                    ac.course_name AS `Course Name`,
                    ac.course_description AS Description,
                    ac.credits AS Credits
                FROM UserCourseProgress ucp
                LEFT JOIN AcademicCourses ac 
                    ON ucp.department = ac.department AND ucp.course_number = ac.course_number
                WHERE ucp.user_id = %s AND ucp.progress_status = 'in-progress'
            """, (user_id,))
            current_courses = cursor.fetchall()

            # Fetch completed courses
            cursor.execute("""
                SELECT 
                    ucp.department AS Department, 
                    ucp.course_number AS `Course Number`,
                    ac.course_name AS `Course Name`,
                    ac.course_description AS Description,
                    ac.credits AS Credits
                FROM UserCourseProgress ucp
                LEFT JOIN AcademicCourses ac 
                    ON ucp.department = ac.department AND ucp.course_number = ac.course_number
                WHERE ucp.user_id = %s AND ucp.progress_status = 'completed'
            """, (user_id,))
            completed_courses = cursor.fetchall()

            # Fetch required courses (not-started) based on CareerPathCourses
            cursor.execute("""
                SELECT 
                    cpc.department AS Department,
                    cpc.course_number AS `Course Number`,
                    ac.course_name AS `Course Name`,
                    ac.course_description AS Description,
                    ac.credits AS Credits
                FROM CareerPathCourses cpc
                LEFT JOIN AcademicCourses ac 
                    ON cpc.department = ac.department AND cpc.course_number = ac.course_number
                WHERE cpc.career_path_id IN (
                    SELECT career_path_id 
                    FROM UserCareerProgress 
                    WHERE user_id = %s
                ) AND CONCAT(cpc.department, cpc.course_number) NOT IN (
                    SELECT CONCAT(department, course_number)
                    FROM UserCourseProgress
                    WHERE user_id = %s
                )
            """, (user_id, user_id))
            required_courses = cursor.fetchall()

        # Return the data in the required format
        return jsonify({
            "status": "success",
            "current": current_courses,
            "completed": completed_courses,
            "required": required_courses
        })
    except Exception as e:
        current_app.logger.error(f"Error fetching academic progress: {e}")
        return jsonify({"error": "An error occurred while fetching academic progression."}), 500
