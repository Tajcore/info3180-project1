from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
SECRET_KEY = os.urandom(32)
UPLOAD_FOLDER = './app/static/Profile_Pictures'

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://whdrjgrihrhabz:372a621310977c01b4e828756de70e321b360c055203bdea1d771fcf1b696cb9@ec2-23-20-129-146.compute-1.amazonaws.com:5432/dbcgs1qd7ovmup"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
