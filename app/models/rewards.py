from .. import db

class RewardTransaction(db.Model):
    __tablename__ = 'rewards'
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String(64))
    points = db.Column(db.Integer)
    transaction_type = db.Column(db.String(20))
    description = db.Column(db.String(200))