from web.extensions import db


class Appointment(db.Model):
    appointment_id = db.Column(db.Integer, primary_key=True)
    appointment_name = db.Column(db.String(20),  nullable=False)
    doctor_name = db.Column(db.String(20),  nullable=False)
    patient_name = db.Column(db.String(20),  nullable=False)
    date = db.Column(db.Date,  nullable=False)

