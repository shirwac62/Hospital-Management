from web.extensions import db


class Prescribes(db.Model):
    Prescribes_id = db.Column(db.Integer, primary_key=True)
    doc_full_name = db.Column(db.String(20),nullable=False)
    pat_full_name = db.Column(db.String(20), nullable=False)
    med_code = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    appointment_name = db.Column(db.String(20), nullable=False)
    dose = db.Column(db.String,  nullable=False)
