from flask import Flask

# to create flask application
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hcfgdhgfj ghdgdgdg'
    
    from .templates.views import views
    from .templates.auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app