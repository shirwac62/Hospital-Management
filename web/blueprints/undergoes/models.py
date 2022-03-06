from web.extensions import db


class Undergoes(db.Model):
    doctor_id = db.Column(db.Integer, primary_key=True)
    doc_first_name = db.Column(db.String(20), unique=True, nullable=False)
    doc_last_name = db.Column(db.String(20), unique=True, nullable=False)

    patient_id = db.Column(db.Integer, primary_key=True)
    pat_first_name = db.Column(db.String(20), unique=True, nullable=False)
    pat_last_name = db.Column(db.String(20), unique=True, nullable=False)
    procedure_code = db.Column(db.Integer, unique=False, nullable=False)
    date = db.Column(db.Integer, unique=False, nullable=False)

    nurse_id = db.Column(db.Integer, primary_key=True)
    nurse_first_name = db.Column(db.String(20), unique=True, nullable=False)
    nurse_last_name = db.Column(db.String(20), unique=True, nullable=False)

    room_no = db.Column(db.Integer,  nullable=False)

