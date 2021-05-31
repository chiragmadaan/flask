from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class Users(db.Model):
    """docstring for User"""
    id = db.Column(db.Integer(), primary_key=True)
    firstname = db.Column(db.String(length=15), nullable=False)
    lastname = db.Column(db.String(length=15))
    email = db.Column(db.String(length=30), unique=True)
    phone_number = db.Column(db.String(length=10))

    def __repr__(self):
        return f'{self.firstname} {self.lastname}'
        

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/login")
def login_page():
    options = {
        "facebook": "fb.com",
        "google": "google.com",
        "email": "dummy"
    }
    return render_template('login.html', data=options)