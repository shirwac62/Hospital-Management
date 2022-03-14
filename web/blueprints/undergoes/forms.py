
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField, DateTimeLocalField, DateField
from wtforms.validators import DataRequired, Length
from utility.util_common import get_all
from utility.util_wtforms import FilterForm
from web.blueprints.doctor.forms import DoctorForm
from web.blueprints.doctor.models import Doctor
from web.blueprints.nurse.models import Nurse
from web.blueprints.patient.models import Patient
from web.blueprints.procedure.models import Procedure
from web.blueprints.room.models import Room
from web.blueprints.undergoes.models import Undergoes


class UndergoesForm(FlaskForm):
    # doctor_first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    doc_full_name = SelectField(choices=[], coerce=str)
    pat_full_name = SelectField(choices=[], coerce=str)
    procedure_code = SelectField(choices=[], coerce=str)
    name = SelectField(choices=[], coerce=str)
    room_no = SelectField(choices=[], coerce=str)
    date = DateField('Start Date', format='%Y-%m-%d')
    submit = SubmitField('Add Doctor')

    def __init__(self, *args, **kwargs):
        super(UndergoesForm, self).__init__()
        # self.doc_full_name.choices = [(0, "Select Doctor")] + [(a.doc_full_name, str(a)) for a in get_all(Doctor)]
        self.doc_full_name.choices = [(0, "Select Doctor")] + [(a.doc_full_name,a.doc_full_name) for a in get_all(Doctor) ]
        self.pat_full_name.choices = [(0, "Select Patient")] + [(a.pat_full_name,a.pat_full_name) for a in get_all(Patient) ]
        self.procedure_code.choices = [(0, "Select Procedure")] + [(a.procedure_code,a.procedure_code) for a in get_all(Procedure) ]
        self.name.choices = [(0, "Select nurse")] + [(a.name,a.name) for a in get_all(Nurse) ]
        self.room_no.choices = [(0, "Select room")] + [(a.room_no,a.room_no) for a in get_all(Room) ]

