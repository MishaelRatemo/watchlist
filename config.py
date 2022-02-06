# import os
# from instance.config import MOVIE_API_KEY
# class Config:
#     '''
#     General configuration parent class
#     '''
#     MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    



# class ProdConfig(Config):
#     '''
#     Production  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''
#     pass


# class DevConfig(Config):
#     '''
#     Development  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''

#     DEBUG = True
    
import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/watchlist'
    #specify the destination  where you want to store  Images.
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/watchlist_test'
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/watchlist'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

