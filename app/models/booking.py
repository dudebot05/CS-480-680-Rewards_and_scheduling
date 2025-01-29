from .. import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    service_type = db.Column(db.String(50))
    booking_date = db.Column(db.DateTime)
    status = db.Column(db.String(20), default='Pending')
    points_earned = db.Column(db.Integer, default=0)
    total_amount = db.Column(db.Float)

    def calculate_points(self):
        return int(self.total_amount * 0.1)