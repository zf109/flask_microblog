"""
    Configuration file for the app
"""

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# openid configurations (depreciated, because OAuth is more popular now)
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]

# SQL alchemy configurations
SQLALCHEMY_DATABASE_URI = 'postgresql://microblog_user:microblog_password@localhost:5432/microblog'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# OAuth configurations
OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '470154729788964',
        'secret': '010cc08bd4f51e34f3f3e684fbdea8a7'
    },
    'twitter': {
        'id': '3RzWQclolxWZIMq5LJqzRZPTl',
        'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
    }
}
