from app import app, db
from flask import render_template, request, redirect, url_for, flash
from .forms import profileForm
from app.models import UserProfile
from werkzeug.utils import secure_filename
import os
###
# Routing for application.
###


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Tahjyei Thompson")

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = profileForm()
    if request.method == 'POST':
            if form.validate_on_submit():
                firstname = form.firstname.data
                lastname = form.lastname.data
                gender = form.gender.data
                email = form.email.data
                location = form.location.data
                biography = form.biography.data
                photo = form.photo.data
                filename = secure_filename(photo.filename)
                photo.save(os.path.join(
                    app.config['UPLOAD_FOLDER'], filename
                ))
                
                profile = UserProfile(firstname, lastname, gender, email, location, biography, filename)
                db.session.add(profile)
                db.session.commit()
                flash('User created successfully', 'success')
                return render_template('result.html',
                                        firstname=firstname,
                                        lastname=lastname,
                                        gender=gender,
                                        email=email,
                                        location=location,
                                        biography=biography
                                        )
            flash_errors(form)
    return render_template('profile.html',
                            form = form,
                            data = [{'gender':'Male'},{'gender':'Female'},{'gender':'Non-Binary'}])


@app.route('/profiles')
def profiles():
    """Retrieve all profiles from the database, then display them"""
    profiles = db.session.query(UserProfile).all()
    update_filepaths(profiles)
    return render_template("profiles.html", profiles = profiles)




def update_filepaths(profiles):
    """Add complete filepath to filenames from database"""
    if type(profiles) != list:
        profiles = [profiles]
    for profile in profiles:
        profile.profile_picture = 'Profile_Pictures/' + profile.profile_picture

def format_date(profiles):
    """Format date string to format {month} {day}, {year}"""
    if type(profiles) != list:
        profiles = [profiles]
    for profile in profiles:
        dte = profile.date_created
        profile.date_created = dte.strftime("%B %d, %Y")       


@app.route('/profile/<userid>')
def view_profile(userid):
    """Query database for complete user info for id, then pass to a template to render the info"""
    profile = db.session.query(UserProfile).get(userid)
    if profile:
        update_filepaths(profile)
        format_date(profile)
        return render_template("profile_details.html", profile = profile)
    else:
        return redirect(url_for("view_profiles")) 
        
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

if __name__ == '__main__':
    app.run(debug=True)
