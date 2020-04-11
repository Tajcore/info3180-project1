from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea

class profileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    location = StringField('Location', validators=[DataRequired()])
    biography = StringField('Biography', validators=[DataRequired()], widget= TextArea())
    photo = FileField('Profile Picture', validators=[FileRequired(),
        FileAllowed(['jpg','png','jpeg'], 'Images only!')])