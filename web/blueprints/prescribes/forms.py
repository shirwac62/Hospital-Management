from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField, DateField, StringField
from wtforms.validators import DataRequired, Length

from utility.util_common import get_all
from web.blueprints.appointment.models import Appointment
from web.blueprints.doctor.models import Doctor
from web.blueprints.medication.models import Medication
from web.blueprints.patient.models import Patient


# class PrescribesForm(FlaskForm):
#     doc_full_name = StringField('Doc Full name', validators=[DataRequired(), Length(min=2, max=30)])
#     pat_full_name = StringField('Pat Full Name', validators=[DataRequired()])
#     med_code = StringField('Code', validators=[DataRequired()])
#     appointment_name = IntegerField('Appointment ID', validators=[DataRequired()])
#     date = IntegerField('Date', validators=[DataRequired()])
#     dose = IntegerField('Dose', validators=[DataRequired()])
#     submit = SubmitField('Add Prescribes')


class PrescribesForm(FlaskForm):
    doc_full_name = SelectField(choices=[], coerce=str)
    pat_full_name = SelectField(choices=[], coerce=str)
    med_code = SelectField(choices=[], coerce=str)
    appointment_name = SelectField(choices=[], coerce=str)
    date = DateField('Start Date', format='%Y-%m-%d')
    dose = IntegerField('dose ', validators=[DataRequired()])
    submit = SubmitField('Add Prescribes')

    def __init__(self, *args, **kwargs):
        super(PrescribesForm, self).__init__()
        # self.doc_full_name.choices = [(0, "Select Doctor")] + [(a.doc_full_name, str(a)) for a in get_all(Doctor)]
        self.doc_full_name.choices = [(0, "Select Doctor")] + [(a.doc_full_name, a.doc_full_name) for a in
                                                               get_all(Doctor)]
        self.pat_full_name.choices = [(0, "Select Patient")] + [(a.pat_full_name, a.pat_full_name) for a in
                                                                get_all(Patient)]
        self.med_code.choices = [(0, "Select Medication")] + [(a.code, a.code) for a in get_all(Medication)]
        self.appointment_name.choices = [(0, "Select Appointment")] + [(a.appointment_name, a.appointment_name) for a in
                                                                       get_all(Appointment)]
