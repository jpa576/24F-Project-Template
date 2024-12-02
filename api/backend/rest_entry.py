from flask import Flask

from backend.CsClasses.Academic_classes_routes import courses
from backend.db_connection import db
from backend.Tech_Skills.Tech_Skill_routes import tech_skills
from backend.Tech_Careers.Career_routes import careers
from backend.products.products_routes import products
from backend.simple.simple_routes import simple_routes
import os
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)

    # Load environment variables from .env file
    load_dotenv()

    # Configure secret key
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Configure MySQL connection
    app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_USER')
    app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_HOST')  # Should resolve to 'algonauts_mysql'
    app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('MYSQL_PORT')) # Ensure this is an integer
    app.config['MYSQL_DATABASE_NAME'] = os.getenv('MYSQL_DATABASE')
    # Initialize the database object with the settings above
    app.logger.info('Starting the database connection')
    db.init_app(app)

    # Register the routes from each Blueprint with the app object
    app.logger.info('Registering blueprints with Flask app object.')
    app.register_blueprint(simple_routes)
    app.register_blueprint(products, url_prefix='/p')
    app.register_blueprint(courses, url_prefix='/c')
    app.register_blueprint(tech_skills, url_prefix='/ts')
    app.register_blueprint(careers, url_prefix='/careers')

    return app
