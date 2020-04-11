from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
SECRET_KEY = os.urandom(32)
UPLOAD_FOLDER = './app/static/Profile_Pictures'

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://pkmlezjsgguodb:98697071ad427262df495a7689b76393d4a6ca3fda3222b60512ae256e9151a8@ec2-34-235-108-68.compute-1.amazonaws.com:5432/d1672ehihq0i6m"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
