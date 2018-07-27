import os

from paypalC2Faq import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand


app = create_app(os.getenv('FLASK_ENV') or 'development')
manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
