import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.secret_key = b'\x08\x13\x0c\x8e\xf1\x81\x84S\xb2:1\xa3\xcb\xe9\xdc\xba'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'paypalC2Faq.db')

app.config['DEBUG'] = True
db = SQLAlchemy(app)
