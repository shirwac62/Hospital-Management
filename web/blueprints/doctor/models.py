from web.extensions import db


class doctor(db.Model):
    doctor_id = db.Column(db.Integer, primary_key=True)
    doc_first_name = db.Column(db.String(20), unique=True, nullable=False)
    doc_last_name = db.Column(db.String(20), unique=True, nullable=False)
    doc_address = db.Column(db.String(20), unique=True, nullable=False)
    doc_ph_no = db.Column(db.Integer, unique=False, nullable=False)
