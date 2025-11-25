from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.models import User,Post 
from flaskblog.forms import RegistrationForm, LoginForm

@app.route('/')
def index():
    return render_template('home.html')


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)