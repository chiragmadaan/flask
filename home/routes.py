from home import app, db
from flask import render_template, redirect, url_for, flash, jsonify, g, request, make_response
from home.models import Users
from home.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, current_user
# from flask_login import login_required
# from werkzeug.security import generate_password_hash, check_password_hash
# import jwt
# import datetime
import flask_sijax
import time


@app.route("/", methods=['GET', 'POST'])
def home_page():
    # if current_user.is_authenticated:
    #     return render_template('home.html')
    # else:
    registration_form = RegistrationForm()
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print("Validating login form inside home_page")
        print(f'request.form => {request.form}')
        # print(f'dir request => {dir(request)}')
        print(f'request.data => {request.data}')
        print(f'request.content_type => {request.content_type}')
        print(f'request.mimetype => {request.mimetype}')
        print(f'request.is_json => {request.is_json}')
        print(f'request.get_json() => {request.get_json()}')
        print(f'request.get_data() => {request.get_data()}')
        print(f'request.args => {request.args}')
        print(f'request.authorization => {request.authorization}')
        print(f'request.base_url => {request.base_url}')
        print(f'request.blueprint => {request.blueprint}')
        print(f'request.cookies => {request.cookies}')
        print(f'request.date => {request.date}')
        print(f'request.endpoint => {request.endpoint}')
        print(f'request.environ => {request.environ}')
        print(f'request.files => {request.files}')
        print(f'request.full_path => {request.full_path}')
        print(f'request.headers => {request.headers}')
        print(f'request.host => {request.host}')
        print(f'request.host_url => {request.host_url}')
        print(f'request.json => {request.json}')
        print(f'request.json_module => {request.json_module}')
        print(f'request.origin => {request.origin}')
        print(f'request.path => {request.path}')
        print(f'request.query_string => {request.query_string}')
        print(f'request.remote_addr => {request.remote_addr}')
        print(f'request.remote_user => {request.remote_user}')
        print(f'request.root_path => {request.root_path}')
        print(f'request.root_url => {request.root_url}')
        print(f'request.server => {request.server}')
        print(f'request.url => {request.url}')
        print(f'request.url_rule => {request.url_rule}')
        print(f'request.url_root => {request.url_root}')
        print(f'request.values => {request.values}')
        print(f'request.view_args => {request.view_args}')
        user = Users.query.filter_by(email=login_form.email.data).first()
        if user and user.verify_password(login_form.password.data):
            login_user(user)
            flash(f'Success! You\'re logged in as: {user.firstname} {user.lastname}', category='success')
            return redirect(url_for('home_page'))
        else:
            flash('Incorrect email ID or password. Please try again.', category='danger')
    if registration_form.validate_on_submit():
        print("validating registration form")
    return render_template('home.html', login_form=login_form, registration_form=registration_form)

#
# @app.route('/', subdomain='practice')
# def practice():
#     return "Coding Practice Page"


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
    registration_form = RegistrationForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            flash(f'Success! You\'re logged in as: {user.firstname} {user.lastname}', category='success')
            return redirect(url_for('home_page'))
        else:
            flash('Incorrect email ID or password. Please try again.', category='danger')
    return render_template('login.html', form=form, login_form=form, registration_form=registration_form)


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


@app.route("/api", methods=['GET', 'POST'])
def api():
    # auth = request.authorization
    #
    # if not auth or not auth.username or not auth.password:
    #     return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
    #
    # user = User.query.filter_by(email=auth.username).first()
    #
    # if not user:
    #     return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
    #
    # if check_password_hash(user.password, auth.password):
    #     token = jwt.encode(
    #         {'public_id': user.public_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
    #         app.config['SECRET_KEY'])
    #
    #     return jsonify({'token': token.decode('UTF-8')})
    #
    # return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if request.method == 'POST':
        print(request.get_json())
        print(request.get_data())
        res = make_response(jsonify({"status": "POST called with" + request.form['param']}), 200)
        return res
    else:
        print(len(request.args))
        print(type(request.args))
        print(request.get_json())
        print(request.get_data())
        print(request.args.get('name'))
        print(request.args.get('last'))
        print(request.args.keys())
        return jsonify({"status": "GET called with"})


@app.route("/api/friends", methods=['GET', 'POST', 'PUT', 'DELETE'])
def friends_utility():
    if request.method == 'GET':
        friends = list()
        friend = dict()
        friend['firstname'] = 'Shray'
        friend['lastname'] = 'Chawla'
        friend['dob'] = '02/09/1989'
        friend['location'] = 'Gurgaon'
        friends.append(friend.copy())
        friend.clear()
        friend['firstname'] = 'Bhisham'
        friend['lastname'] = 'Gudwani'
        friend['dob'] = '01/12/1989'
        friend['location'] = 'San Francisco'
        friends.append(friend.copy())
        friend.clear()
        friend['firstname'] = 'Rahul'
        friend['lastname'] = 'Dahra'
        friend['dob'] = '08/08/1989'
        friend['location'] = 'Gurgaon'
        friends.append(friend.copy())
        del friend
        return jsonify(friends)
    elif request.method == 'POST':
        return jsonify('{"error":"Friends creation not yet implemented"}')
    elif request.method == 'PUT':
        return jsonify('{"error":"Friends editing not yet implemented"}')
    elif request.method == 'DELETE':
        return jsonify('{"error":"Friends deleting not yet implemented"}')


@app.route("/login_ajax", methods=['GET', 'POST'])
def ajax_login():
    if request.method == 'POST':
        print(f'request.form => {request.form}')
        # print(f'dir request => {dir(request)}')
        print(f'request.data => {request.data}')
        print(f'request.content_type => {request.content_type}')
        print(f'request.mimetype => {request.mimetype}')
        print(f'request.is_json => {request.is_json}')
        print(f'request.get_json() => {request.get_json()}')
        print(f'request.get_data() => {request.get_data()}')
        print(f'request.args => {request.args}')
        print(f'request.authorization => {request.authorization}')
        print(f'request.base_url => {request.base_url}')
        print(f'request.blueprint => {request.blueprint}')
        print(f'request.cookies => {request.cookies}')
        print(f'request.date => {request.date}')
        print(f'request.endpoint => {request.endpoint}')
        print(f'request.environ => {request.environ}')
        print(f'request.files => {request.files}')
        print(f'request.full_path => {request.full_path}')
        print(f'request.headers => {request.headers}')
        print(f'request.host => {request.host}')
        print(f'request.host_url => {request.host_url}')
        print(f'request.json => {request.json}')
        print(f'request.json_module => {request.json_module}')
        print(f'request.origin => {request.origin}')
        print(f'request.path => {request.path}')
        print(f'request.query_string => {request.query_string}')
        print(f'request.remote_addr => {request.remote_addr}')
        print(f'request.remote_user => {request.remote_user}')
        print(f'request.root_path => {request.root_path}')
        print(f'request.root_url => {request.root_url}')
        print(f'request.server => {request.server}')
        print(f'request.url => {request.url}')
        print(f'request.url_rule => {request.url_rule}')
        print(f'request.url_root => {request.url_root}')
        print(f'request.values => {request.values}')
        print(f'request.view_args => {request.view_args}')

        login_form = LoginForm()
        print(login_form.is_submitted())
        print(login_form.validate())
        print(dir(login_form))
        print(login_form.data)

        # reg_form = RegistrationForm()
        # print(reg_form.is_submitted())
        # print(reg_form.validate())
        # print(dir(reg_form))
        # print(reg_form.data)

        if login_form.validate_on_submit():
            user = Users.query.filter_by(email=login_form.email.data).first()
            if user and user.verify_password(login_form.password.data):
                login_user(user)
                flash(f'Success! You\'re logged in as: {user.firstname} {user.lastname}', category='success')
                # return redirect(url_for('home_page'))
                return jsonify(message=f'Success! You\'re logged in as: {user.firstname} {user.lastname}'), 200
            else:
                flash('Incorrect email ID or password. Please try again.', category='danger')
                return jsonify(message=f'Incorrect email ID or password. Please try again.'), 401

        return jsonify(message="POST API is up and running!"), 444
    elif request.method == 'GET':
        return jsonify(message="GET API is up and running!")


@app.route("/test")
def test():
    return render_template('test.html')
#
#
# @flask_sijax.route(app, '/flask-login')
# def hello():
#     # Every Sijax handler function (like this one) receives at least
#     # one parameter automatically, much like Python passes `self`
#     # to object methods.
#     # The `obj_response` parameter is the function's way of talking
#     # back to the browser
#     def say_hi(obj_response):
#         # obj_response.alert('Hi there!')
#         print('Hi there!')
#         obj_response.html('#messages', '')
#         obj_response.attr('#message', 'value', '')
#         obj_response.script("$('#message').focus();")
#
#     def login(obj_response, email, password):
#         obj_response.alert(f'Trying to login with {email} and {password}')
#
#     def register(obj_response, email, password):
#         obj_response.alert(f'Trying to register with {email} and {password}')
#
#     if g.sijax.is_sijax_request:
#         # Sijax request detected - let Sijax handle it
#         g.sijax.register_callback('say_hi', say_hi)
#         g.sijax.register_callback('sijax-login', login)
#         g.sijax.register_callback('sijax-register', register)
#         return g.sijax.process_request()
#
#     registration_form = RegistrationForm()
#     login_form = LoginForm()
#     return render_template('home.html', login_form=login_form, registration_form=registration_form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#
# @app.cli.command('db_create')
# def create_db():
#     # command to run 'flask db_create'
#     db.create_all()
#     print('Database created!')
#
#
# @app.cli.command('db_drop')
# def drop_db():
#     # command to run 'flask db_drop'
#     db.drop_all()
#     print('Database dropped!')
