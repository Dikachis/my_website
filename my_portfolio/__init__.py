from flask import Flask

# to create flask application
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'how are you'

    return app