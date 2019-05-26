from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Columne(db.Integer, primary_key=True)
    username = db.Column(db.String)

    def __repr__(self):
        return 'User {}'.format(self.username)
        