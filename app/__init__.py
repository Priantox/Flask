from flask import Flask, render_template
from app.forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '486a440762160cd1032b6b88a8e90e8c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
