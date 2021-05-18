from flask_script import Manager
from swbpacote import creat_app

manager = Manager(creat_app)

if __name__ == '__main__':
    manager.run()