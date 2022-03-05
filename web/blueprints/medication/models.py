from web.extensions import db


class Medication(db.Model):
    medication_id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(20),  nullable=False)
    name = db.Column(db.String(20),  nullable=False)
    brand = db.Column(db.String(20),  nullable=False)
    description = db.Column(db.String(20),   nullable=False)

