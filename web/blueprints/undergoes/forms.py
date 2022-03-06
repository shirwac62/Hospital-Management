from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length

from utility.util_common import get_all
from web.blueprints.doctor.forms import DoctorForm
from web.blueprints.doctor.models import Doctor


class UndergoesForm(FlaskForm):
    # doctor_first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    doctor_first_name = SelectField(choices=[], coerce=str, validators=[DataRequired(), Length(min=2, max=20)])
    doctor_last_name = StringField('Last Name', validators=[DataRequired()])
    pat_first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    pat_last_name = StringField('Last Name', validators=[DataRequired()])
    procedure_code = IntegerField('Procedure Code', validators=[DataRequired()])
    nurse_first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    nurse_last_name = StringField('Last Name', validators=[DataRequired()])
    room_no = IntegerField('Room No', validators=[DataRequired()])
    date = IntegerField('date ', validators=[DataRequired()])

    def init(self, *args, **kwargs):
        super(UndergoesForm, self).init(*args, **kwargs)
        self.doctor_first_name.choices = [(0, "Doctor Name")] + [(a.doctor_first_name, str(a)) for a in get_all(Doctor)]


