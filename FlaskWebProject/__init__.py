"""
The flask application package.
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import logging

app = Flask(__name__)
app.config.from_object(Config)

# Logging setup
logging.basicConfig(level=logging.INFO)

db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = 'login'

from FlaskWebProject import views, models