from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_simplemde import SimpleMDE
simple = SimpleMDE()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
db = SQLAlchemy()

# Initializing app
def create_app(config_name):

    app = Flask(__name__, instance_relative_config=False)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.config['UPLOAD_PATH'] = 'app/static/photos'
   

    # Initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    simple.init_app(app)
    # configure UploadSet
    bootstrap = Bootstrap(app)
    

    with app.app_context():
        # Registering main blueprint
        from .main import main as main_blueprint
        app.register_blueprint(main_blueprint, url_prefix = '/main')

        #Register auth blueprint
        from .auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    
        # # Create Database Models
        db.drop_all()
        db.create_all()
    return app