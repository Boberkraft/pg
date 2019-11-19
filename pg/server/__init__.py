__all__ = ['app']
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask import Flask
from pg.server import db

DATABASE_PATH = 'test.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DATABASE_PATH}"

db.init_app(app)



