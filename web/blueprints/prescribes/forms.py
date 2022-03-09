from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, DateTimeLocalField, SubmitField
from wtforms.validators import DataRequired



class PrescribesForm(FlaskForm):
    doc_full_name = SelectField(choices=[], coerce=str)
    pat_full_name = SelectField(choices=[], coerce=str)
    med_code = SelectField(choices=[], coerce=str)
    appointment_id = SelectField(choices=[], coerce=str)
    date = DateTimeLocalField('date ', validators=[DataRequired()])
    dose = IntegerField('dose ', validators=[DataRequired()])
    submit = SubmitField('Add Prescribes')


    # def __init__(self, *args, **kwargs):
    #     super(PrescribesForm, self).__init__()
    #     # self.doc_full_name.choices = [(0, "Select Doctor")] + [(a.doc_full_name, str(a)) for a in get_all(Doctor)]
    #     self.doc_full_name.choices = [(0, "Select Doctor")] + [(a.doc_id,a.doc_full_name) for a in get_all(Doctor) ]
    #     self.pat_full_name.choices = [(0, "Select Patient")] + [(a.patient_id,a.pat_full_name) for a in get_all(Patient) ]
    #     self.med_code.choices = [(0, "Select Medication")] + [(a.medication_id,a.med_code) for a in get_all(Medication) ]
    #     self.appointment_id.choices = [(0, "Select Appointment")] + [(a.Appointment_id,a.Appointment_id) for a in get_all(Appointment) ]

