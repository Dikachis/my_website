from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

# to create flask application
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hcfgdhgfj ghdgdgdg'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # initialize database by given it app
    db.init_app(app)
    
    from .templates.views import views
    from .templates.auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .templates.models import User, Note

    create_database(app)

    return app
    
def create_database(app):
    try:
        if not path.exists('my_portfolio/' + DB_NAME):
            db.create_all(app=app)
    except Exception:
        print('Created Database!')
