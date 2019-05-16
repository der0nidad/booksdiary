from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    author = db.Column(db.String(120), index=True, unique=True)
    desription = db.Column(db.String(400))
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Book {} {} user {}>'.format(self.author, self.name, self.uid) 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    books = db.relationship('Book', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class BookItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    author = db.Column(db.String(120), index=True, unique=True)
    desription = db.Column(db.Text())