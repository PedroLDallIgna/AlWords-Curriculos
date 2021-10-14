from flask.templating import render_template
from app import app, db_users, users, data
from app.forms import EditProfile, SignIn, SignUp
from flask import flash, request, redirect, url_for, session
import json

@app.route('/')
def index():
    return render_template("public/index.html", title="Hello, World!")

@app.route('/signin', methods=['POST', 'GET'])
def signin():
    form = SignIn()
    # if request.method == 'POST':
    #     if form.validate() == False:
    #         flash("All fields are required!")
    #         return render_template("public/signin.html", form=form)
    # elif request.method == 'GET':
    #     return render_template("public/signin.html", form=form)
    return render_template('public/signin.html', form=form)

@app.route('/auth', methods=['POST', 'GET'])
def auth():
    # for id in db_users.get_users():
    for user in db_users.get_db():
        if user['email'] == request.form['email'] and user['password'] == request.form['password']:
            session['user_logged'] = user
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('signin'))

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if request.method == 'GET' and not session['user_logged']:
        return redirect(url_for('signin'))
    else:
        return render_template('public/dashboard.html', active_user=session['user_logged'])

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignUp()
    # if request.method == 'POST':
    #     if form.validate_on_submit():
    #         flash('All fields are required')
    #         return redirect(url_for('index'))
    #     else:
    #         return render_template('public/signup.html', form=form)
    # elif request.method == 'GET':
    return render_template("public/signup.html", form=form)

@app.route('/regist', methods=['POST', 'GET'])
def regist():
    user = {
        '_id': '{0:0>5d}'.format(len(db_users.get_users())+1),
        'name': request.form['name'],
        'lastname': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'phone': request.form['phone'],
        'sex': request.form['sex'],
    }
    db_users.update_db(user)
    session['user_logged'] = user
    data.update_db({
        '_user_id': session['user_logged']['_id'],
        'description': "",
        'social_media': {
            'facebook': "",
            'instagram': "",
            'twitter': "",
            'linkedin': "",
            'github': ""
        }
    })
    # return render_template('public/index.html', title='Hello World')
    return redirect(url_for('edit_profile', id=session['user_logged']['_id']))
    # return redirect(url_for('index'))

@app.route('/signout', methods=['POST', 'GET'])
def signout():
    session['user_logged'] = None
    return redirect(url_for('index'))

@app.route('/<id>/profile', methods=['GET'])
def profile(id):
    with open('app/database/users_data.json', 'r') as read_file:
        users_data = json.load(read_file)
    for user in users_data:
        if user['_user_id'] == id:
            user_data = user
            return render_template('public/profile.html', user=[user for user in db_users.get_db() if user['_id'] == id][0], condition=(id if id == session['user_logged']['_id'] else False), user_data=user_data)
    return redirect(url_for('index'))
    # return render_template('public/profile.html', user=[user for user in db_users.get_db() if user['_id'] == id][0], condition=(id if id == session['user_logged']['_id'] else False), user_data=[user for user in users_data.get_db() if user['_user_id'] == id][0])

@app.route('/<id>/profile/edit', methods=['POST', 'GET'])
def edit_profile(id):
    form = EditProfile()
    with open('app/database/users_data.json', 'r') as read_file:
        users_data = json.load(read_file)
    if id == session['user_logged']['_id']:
        for user in users_data:
            if user['_user_id'] == id:
                user_data = user
                # return render_template('public/edit_profile.html', user=[user for user in db_users.get_db() if user['_id'] == id][0], condition=id if id == session['user_logged']['_id'] else False, form=form, user_data=user_data)
                return render_template('public/edit_profile.html', user=session['user_logged'], condition=id if id == session['user_logged']['_id'] else False, form=form, user_data=user_data)
    else:
        return redirect(url_for('profile', id=id))

@app.route('/save-changes', methods=['POST', 'GET'])
def save_changes():
    with open('app/database/users_data.json', 'r') as read_file:
        users_data = json.load(read_file)
    to_append = {
        '_user_id': session['user_logged']['_id'],
        'description': request.form['description'] if request.form['description'] else "",
        'social_media': {
            'facebook': request.form['facebook'] if len(request.form['facebook'])>0 else "",
            'instagram': request.form['instagram'] if request.form['instagram'] else "",
            'twitter': request.form['twitter'] if request.form['twitter'] else "",
            'linkedin': request.form['linkedin'] if request.form['linkedin'] else "",
            'github': request.form['github'] if request.form['github'] else ""
        }
    }
    if len(users_data) > 0:
        for i in range(len(users_data)):
            if users_data[i]['_user_id'] == session['user_logged']['_id']:
                users_data[i] = to_append
    else:
        users_data.append(to_append)
        # users_data.update_db(to_append)
    with open('app/database/users_data.json', 'w') as write_file:
        json.dump(users_data, write_file, indent=4)
    return redirect(url_for('profile', id=session['user_logged']['_id']))

@app.route('/list-users', methods=['GET'])
def list_users():
    return render_template('public/list-users.html', users=[" ".join([user['name'], user['lastname']]) for user in db_users.get_db()])
