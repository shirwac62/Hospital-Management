from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class PatientForm(FlaskForm):
    pat_first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    pat_last_name = StringField('Last Name', validators=[DataRequired()])
    pat_address = StringField('Address', validators=[DataRequired()])
    pat_insurance_no = IntegerField('Insurance No', validators=[DataRequired()])
    pat_ph_no = IntegerField('Phone No', validators=[DataRequired()])
    submit = SubmitField('Add Patient')






