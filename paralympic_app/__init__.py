from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# Create a global SQLAlchemy object
db = SQLAlchemy()
# Create a global Flask-Marshmallow object
ma = Marshmallow()


def create_app(config_object):
    """Create and configure the Flask app"""
    app = Flask(__name__)
    # Config parameters are in config.py
    app.config.from_object(config_object)

    # Uses a helper function to initialise extensions
    initialize_extensions(app)

    with app.app_context():
        # Include the routes from routes.py
        from . import routes

        db.create_all()

    return app


def initialize_extensions(app):
    """Binds extensions to the Flask application instance (app)"""
    # Flask-SQLAlchemy
    db.init_app(app)
    # Flask-Marshmallow
    ma.init_app(app)


# At end to prevent circular imports
from paralympic_app.models import Event, Region
