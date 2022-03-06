from web.extensions import db


class Room(db.Model):
    room_id = db.Column(db.Integer, primary_key=True)
    room_no = db.Column(db.Integer,  nullable=False)
    room_type = db.Column(db.String(20),  nullable=False)
    available = db.Column(db.String(20),  nullable=False)
