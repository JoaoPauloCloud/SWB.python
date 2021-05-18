from flask import Flask, app

def creat_app():
    app = Flask(__name__)

    regiter_blueprints(app)
    
    return app

def regiter_blueprints(app):
    from swbpacote.url import bp_contact

    app.register_blueprint(bp_contact)