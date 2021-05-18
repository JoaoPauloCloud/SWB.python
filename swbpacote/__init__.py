from flask import Flask, app
from flask_bootstrap import Bootstrap

def creat_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'UmaChaveQualquer'
    Bootstrap(app)
    
    regiter_blueprints(app)
    
    return app

def regiter_blueprints(app):
    from swbpacote.url import bp_contact

    app.register_blueprint(bp_contact)