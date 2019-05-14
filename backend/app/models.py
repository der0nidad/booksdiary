from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    author = db.Column(db.String(120), index=True, unique=True)
    desription = db.Column(db.String(400))

    def __repr__(self):
        return '<Book {} {}>'.format(self.author, self.name) 