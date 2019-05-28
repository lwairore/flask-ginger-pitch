from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    password_hash = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitch = db.relationship('Pitch', backref="user", lazy="dynamic")
    user_comment = db.relationship('Comment', backref="user", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

class Pitch(UserMixin,db.Model):
    __tablename__ = 'pitch_table'
    id = db.Column(db.Integer, primary_key=True)
    pitch_title = db.Column(db.String)
    pitch_body = db.Column(db.String)
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    category = db.Column(db.String(255))
    pitch = db.relationship("Comment", backref="user_pitch", lazy="dynamic")
    posted_by = db.Column(db.String)
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    comment = db.Column(db.String)
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitch_table.id"))
    postedAt = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    posted_by = db.Column(db.String)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, id):
        comments = Comment.query.filter_by(pitch_id=id)
        return comments
        

    
