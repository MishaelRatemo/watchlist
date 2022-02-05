from datetime import datetime
from email.policy import default
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin ## helps  to implement the methods ( is_authenticated(), is_active()-, is_anonymous() and get_id())
from . import login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class Movie:
    '''
    Movie class to define Movie Objects
    '''
    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count



class Review(db.Model):
    
    __tablename__ = 'reviews'
    id = db.Column(db.Integer,primary_key = True)
    movie_id = db.Column(db.Integer)
    movie_title = db.Column(db.String)
    image_path = db.Column(db.String)
    movie_review = db.Column(db.String)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))



    def save_review(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_reviews(cls,id):

        response =cls.query.filter_by(movie_id = id).all()
        return response


'''Class allowing us to create new users'''
class User(UserMixin ,db.Model): # db.model arg help us to connect to DB and communicate
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    # creating connection btn Role and User models by use of Foreign Key
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    # colum to hold passwords
    pass_secure = db.Column(db.String(255))
    # password_hash = db.Column(db.String(255))
    
    @property # allows only write only
    def password(self):
        raise AttributeError('You cannot read the password attribute') # raise blocks access to password

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)
    
    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    
    def __repr__(self):
        return f'User {self.username}'
    

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    # create a virtual column that will connect with the foreign key in User
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'