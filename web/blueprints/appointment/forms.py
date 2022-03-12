from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeLocalField, DateField
from wtforms.validators import DataRequired, Length

from utility.util_common import get_all
from web.blueprints.doctor.models import Doctor
from web.blueprints.patient.models import Patient





class AppointmentForm(FlaskForm):
    appointment_name = StringField('Appointment Name', validators=[DataRequired(), Length(min=2, max=20)])
    doctor_name = SelectField(choices=[], coerce=str)
    patient_name = SelectField(choices=[], coerce=str)
    date = DateField('Start Date', format='%Y-%m-%d')
    submit = SubmitField('Add Appointment')



    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__()
        # self.doc_full_name.choices = [(0, "Select Doctor")] + [(a.doc_full_name, str(a)) for a in get_all(Doctor)]
        self.doctor_name.choices = [(0, "Select Doctor")] + [(a.doc_full_name,a.doc_full_name) for a in get_all(Doctor) ]
        self.patient_name.choices = [(0, "Select Patient")] + [(a.pat_full_name,a.pat_full_name) for a in get_all(Patient) ]

