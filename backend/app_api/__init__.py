from flask import Flask, request, jsonify, make_response
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy()
ma = Marshmallow()

# Initializing app
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    #initialize extensions
    db.init_app(app)  
    ma.init_app(app)  
    with app.app_context():
        # Registering main blueprint
        from main import main as main_blueprint
        app.register_blueprint(main_blueprint, url_prefix = '/main')

    
    
        # # Create Database Models
     
    return app