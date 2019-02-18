from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'marcos'}
    posts = [
        {
            'author': {'username':'John'},
            'body' : 'Beautiful day in Poland'
        },
        {
            'author' : {'username' : 'Susan'},
            'body' : 'The Avengers movie was so cool!'
        },
        {
            'author': {'username' : 'Marcos'},
            'body' : 'Nobody cares what you think.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/info')
def info():
    return '<h1>My Bio Dude!</h1>'
