from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class doctorForm(FlaskForm):
    doctor_first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    doctor_last_name = StringField('Last Name', validators=[DataRequired()])
    doctor_address = StringField('Address', validators=[DataRequired()])
    doctor_ph_no = IntegerField('Phone No', validators=[DataRequired()])
    submit = SubmitField('Add doctor')
