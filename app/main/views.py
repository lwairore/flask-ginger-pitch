from . import main
from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required, current_user
from ..models import User, Pitch
from .forms import UpdateProfile, PitchForm
from .. import db, photos

@main.route('/')
def index():
    title = "Pitch | Home"
    return render_template('index.html', title = title)

@main.route("/new/pitch")
@login_required
def new_post():
    title = "Create Pitch"
    return render_template("new_pitch.html", title=title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)

@main.route('/user/<uname>/update', methods=["GET","POST"])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)

@main.route('/user/<uname>/update/pic', methods=["POST"])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = 'photos/{}'.format(filename)
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))

@main.route('/new/pitch', methods=["GET","POST"])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data

        # Update Pitch
        new_pitch = Pitch(pitch_title=title, pitch_body=pitch, user=current_user)

        # Save Pitch 
        new_pitch.save_pitch()
        return redirect(url_for('.user_pitch',uname=current_user))
    title = "Pitch | New"
    user = current_user
    user_details = User.query.filter_by(username=user).first()
    return render_template('new_pitch.html', title=title, pitch_form=form, user=user_details)

@main.route('/<uname>/pitch>')
@login_required
def user_pitch(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    return render_template("pitch/user_pitch.html", user=user)