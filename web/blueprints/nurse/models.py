from web.extensions import db


class Nurse(db.Model):
    nurse_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    nurse_address = db.Column(db.String(20), unique=True, nullable=False)
    nurse_ph_no = db.Column(db.Integer, unique=False, nullable=False)


