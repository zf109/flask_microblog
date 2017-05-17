from flask import render_template, flash, redirect, get_flashed_messages
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    """Index page """
    user = {'nickname': 'EvilerPizza'} # Test
    posts = [ # Fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in London!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The new movie looks interesting!'
        },
        {
            'author': user,
            'body': 'The pizza is getting eviler...'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page """
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s'%(form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form, providers=app.config['OPENID_PROVIDERS'])

