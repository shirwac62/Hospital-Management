from web.extensions import db


class Prescribes(db.Model):
    Prescribes_id = db.Column(db.Integer, primary_key=True)
    doc_full_name = db.Column(db.String(20),nullable=False)
    pat_full_name = db.Column(db.String(20), nullable=False)
    Med_Code = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    appointment_ID = db.Column(db.Integer, nullable=False)
    dose = db.Column(db.Integer,  nullable=False)
