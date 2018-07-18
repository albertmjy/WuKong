import os

from paypalC2Faq import create_app
from flask_script import Manager

app = create_app(os.getenv('PAYPALC2FAQ_ENV') or 'dev')
manager = Manager(app)


if __name__ == '__main__':
    manager.run()

