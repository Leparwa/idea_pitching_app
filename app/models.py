from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users_table'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('user_roles.id'))
    pass_secure  = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pitch_desc = db.relationship('Pitch',backref = 'user',lazy = "dynamic")

    def __repr__(self):
        return f'User {self.username}'


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


class Role(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer,primary_key = True)
    role = db.Column(db.String(255))
    users = db.relationship('User',backref = 'user_role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.role}'

class Pitch(db.Model):

    __tablename__ = 'user_pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String)
    pitch_image_path = db.Column(db.String)
    pitch_desc = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users_table.id"))

   
        
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

