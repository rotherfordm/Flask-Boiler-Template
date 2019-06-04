from app import db, app


class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parameter1 = db.Column(db.Float())
    parameter2 = db.Column(db.Float())
