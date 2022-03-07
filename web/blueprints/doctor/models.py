from web.extensions import db


class Doctor(db.Model):
    doc_id = db.Column(db.Integer, primary_key=True)
    doc_full_name = db.Column(db.String(30), nullable=False)
    doc_address = db.Column(db.String(20), nullable=False)
    doc_ph_no = db.Column(db.Integer, unique=False, nullable=False)
