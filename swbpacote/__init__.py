from flask import Flask, app
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'UmaChaveQualquer'
    Bootstrap(app)
    db.init_app(app)
    
    regiter_blueprints(app)
    
    return app

def regiter_blueprints(app):
    from swbpacote.url import bp_contact

    app.register_blueprint(bp_contact)