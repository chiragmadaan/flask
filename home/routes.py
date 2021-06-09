from home import app, db
from flask import render_template, redirect, url_for, flash, jsonify, g
from home.models import Users
from home.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user
# from flask_login import login_required


@app.route("/")
def home_page():
    return render_template('home.html')


@app.route("/register", methods=['GET', 'POST'])
def registration_page():
    # options = Users.query.all()
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, phone_number=form.phone_number.data, password=form.password1.data)
        # # user = Users(email=form.email.data, password_hash=form.password1.data)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash(f'Success! You\'re logged in as: {user.firstname} {user.lastname}', category='success')

        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(err, category='danger')
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            flash(f'Success! You\'re logged in as: {user.firstname} {user.lastname}', category='success')
            return redirect(url_for('home_page'))
        else:
            flash('Incorrect email ID or password. Please try again.', category='danger')
    return render_template('login.html', form=form)


@app.route("/logout")
def logout_page():
    logout_user()
    flash('You have been logged out', category='info')
    return redirect(url_for('home_page'))


# @app.route("/<name>")
# def random_page(name="poo"):
#     return f'Hi, {name}'


@app.route("/data")
def get_data():
    return 'Hi from data'


@app.route("/test")
def test():
    return render_template('test.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
