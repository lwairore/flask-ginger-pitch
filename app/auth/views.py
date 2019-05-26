from flask import render_template, redirect, url_for, flash, request
from . import auth
from ..models import User
from .forms import RegistrationForm, LoginForm
from  .. import db

@auth.route('/login')
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).firts()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid Username or Password!')

    title = "Pitch | Sign-in"
    return render_template('auth/login.html', title=title)

@auth.route('/register', methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    title = 'Pitch | New Account'
    return render_template('/auth/register.html', registration_form=form)
