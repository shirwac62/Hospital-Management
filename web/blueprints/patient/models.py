from web.extensions import db


class Patient(db.Model):
    patient_id = db.Column(db.Integer, primary_key=True)
    pat_full_name = db.Column(db.String(20), nullable=False)
    pat_address = db.Column(db.String(20), nullable=False)
    pat_insurance_no = db.Column(db.Integer, nullable=False)
    pat_ph_no = db.Column(db.Integer, unique=False, nullable=False)








