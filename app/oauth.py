"""
    Oauth module for the app.
"""
from app import app
from flask import url_for, redirect
from rauth import OAuth1Service, OAuth2Service

class OAuthSignIn(object):
    """ OAuth signin base class """
    providers = None

    def __init__(self, provider_name):
        self.provider_name = provider_name
        credentials = app.config['OAUTH_CREDENTIALS'][provider_name]
        self.consumer_id = credentials['id']
        self.consumer_secret = credentials['secret']

    def authorize(self):
        """Authorisation abstract method """
        pass

    def callback(self):
        """Callback abstract method """
        pass

    def get_callback_url(self):
        """Helper function get the allback url """
        return url_for('oauth_callback', provider=self.provider_name,
                       _external=True)
    
    @classmethod
    def get_provider(self, provider_name):
        if self.providers is None:
            self.providers = {}
            for provider_class in self.__subclasses__():
                provider = provider_class()
                self.providers[provider.provider_name] = provider
        return self.providers[provider_name]


class FacebookSignIn(OAuthSignIn):
    def __init__(self):
        super(FacebookSignIn, self).__init__('facebook')
        self.service = OAuth2Service(
            client_id=self.consumer_id,
            client_secret=self.consumer_secret,
            authorize_url='https://graph.facebook.com/oauth/authorize',           
            access_token_url='https://graph.facebook.com/oauth/access_token',
            base_url='https://graph.facebook.com/'
        )
    
    def authorize(self):
        return redirect(self.service.get_authorize_url(
            scope='email',
            response_type='code',
            redirect_uri=self.get_callback_url())
        )


class TwitterSignIn(OAuthSignIn):
    pass
