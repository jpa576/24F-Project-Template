from flask import Blueprint, request, jsonify, current_app, g
import pymysql
import os

careers = Blueprint('careers', __name__)

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

@careers.teardown_app_request
def close_db_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@careers.route('/all_careers', methods=['GET'])
def get_all_careers():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM CareerPaths")
            data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        current_app.logger.error(f"Error fetching all career paths: {e}")
        return jsonify({"error": "An error occurred while fetching careers."}), 500

@careers.route('/career_skills', methods=['GET'])
def get_career_skills():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                  cp.career_name, ts.skill_name
                FROM
                    CareerPathSkills cps
                    join algonauts_db.CareerPaths cp on cp.career_path_id = cps.career_path_id
                    join algonauts_db.TechSkills ts on ts.tech_skill_id = cps.tech_skill_id
                    order by cp.career_name
                """)
            data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        current_app.logger.error(f"Error fetching data: {e}")
        return jsonify({"error": "An error occurred while fetching data."}), 500

@careers.route('/career_noskills', methods=['GET'])
def get_career_noskills():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    cp.career_name
                FROM
                    algonauts_db.CareerPaths cp
                LEFT JOIN
                    algonauts_db.CareerPathSkills cps ON cp.career_path_id = cps.career_path_id
                WHERE
                    cps.career_path_id IS NULL
                ORDER BY
                    cp.career_name;
            """)
            data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        current_app.logger.error(f"Error fetching careers without skills: {e}")
        return jsonify({"error": "An error occurred while fetching careers without skills."}), 500
