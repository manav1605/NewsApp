from init import db
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String())
    title = db.Column(db.String())
    description = db.Column(db.String())
    category = db.Column(db.String())


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    password = db.Column(db.String())
    favourites = db.Column(db.String())