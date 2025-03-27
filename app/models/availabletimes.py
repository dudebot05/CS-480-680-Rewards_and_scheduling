from .. import db

class AvailableTimes(db.Model):
    __tablename__ = 'available'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    available_start = db.Column(db.DateTime)
    available_end = db.Column(db.DateTime)