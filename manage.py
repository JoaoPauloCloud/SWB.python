from flask_script import Manager
from swbpacote import create_app, db

manager = Manager(create_app)

@manager.command
def init_db():
    db.create_all()

if __name__ == '__main__':
    manager.run()