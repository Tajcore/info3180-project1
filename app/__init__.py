from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
SECRET_KEY = os.urandom(32)
UPLOAD_FOLDER = './app/static/Profile_Pictures'

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://aimdukhdmkhpxj:abaace9533cc39e4a14b25c2693927ed7fe5972fbc1a42987c3987f79baab7df@ec2-54-147-209-121.compute-1.amazonaws.com:5432/dfbhe6ai7ih0cg"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
app.config['UPLOAD_FOLDER'] = './app/static/uploads'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
