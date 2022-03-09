from web.extensions import db


class Appointment(db.Model):
    appointment_name = db.Column(db.string, primary_key=True)
    patient_name = db.Column(db.String(20), unique=True, nullable=False)
    appointment_Date = db.Column(db.integer(20), unique=True, nullable=False)