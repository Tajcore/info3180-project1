from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
SECRET_KEY = os.urandom(32)
UPLOAD_FOLDER = './app/static/Profile_Pictures'

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://yxscqrinjaicrk:63f01346475afadb98dd9635e1410e6becbf30c5d59460aed5c7652ff7510ada@ec2-52-7-39-178.compute-1.amazonaws.com:5432/d5ccae1rhr7fae"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
