from flask.templating import render_template
from app import app, db, users
from app.forms import SignIn, SignUp
from flask import flash, request, redirect, url_for, session

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
    for id in db.get_users():
        for user in db.get_db():
            if user['_id'] == id and user['email'] == request.form['email'] and user['password'] == request.form['password']:
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
        '_id': '{0:0>5d}'.format(len(users)+1),
        'name': request.form['name'],
        'lastname': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'phone': request.form['phone'],
        'sex': request.form['sex'],
    }
    db.update_db(user)
    users.append('{0:0>5d}'.format(len(users)+1))
    # return render_template('public/index.html', title='Hello World')
    return redirect(url_for('index'))

@app.route('/signout', methods=['POST', 'GET'])
def signout():
    session['user_logged'] = None
    return redirect(url_for('index'))

@app.route('/<id>/profile', methods=['GET'])
def profile(id):
    return render_template('public/profile.html', user=[user for user in db.get_db() if user['_id'] == id][0], condition=(id if id == session['user_logged']['_id'] else False))

@app.route('/<id>/profile/edit', methods=['GET'])
def edit_profile(id):
    if id == session['user_logged']['_id']:
        return render_template('public/edit_profile.html', user=[user for user in db.get_db() if user['_id'] == id][0], condition=id if id == session['user_logged']['_id'] else False)
    else:
        return redirect(url_for('profile', id=id))

@app.route('/list-users', methods=['GET'])
def list_users():
    return render_template('public/list-users.html', users=[" ".join([user['name'], user['lastname']]) for user in db.get_db()])
