from flask import Flask
from api.backend.db_connection import db
from api.backend.customers.customer_routes import customers
from api.backend.products.products_routes import products
from api.backend.simple.simple_routes import simple_routes

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
    app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_HOST')
    app.config['MYSQL_DATABASE_PORT'] = int(os.getenv('MYSQL_PORT'))
    app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_NAME')

    # Initialize the database object with the settings above
    app.logger.info('Starting the database connection')
    db.init_app(app)

    # Register the routes from each Blueprint with the app object
    app.logger.info('Registering blueprints with Flask app object.')
    app.register_blueprint(simple_routes)
    app.register_blueprint(customers, url_prefix='/c')
    app.register_blueprint(products, url_prefix='/p')

    return app
