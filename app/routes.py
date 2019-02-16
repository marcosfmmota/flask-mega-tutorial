from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'marcos'}
    return render_template('index.html', title='Home', user=user)

@app.route('/info')
def info():
    return '<h1>My Bio Dude!</h1>'
