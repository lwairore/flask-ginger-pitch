from . import main
from flask import render_template, request, redirect, url_for, abort
from flask_login import login_required
from ..models import Reviews, User
from .forms import UpdateProfile
from .. import db

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
    
    