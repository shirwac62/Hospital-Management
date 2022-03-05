from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class AppointmentForm(FlaskForm):
    patient_name =  StringField('patient Name', validators=[DataRequired()])
    Appointment_name = StringField('Appointment Name', validators=[DataRequired()])
    Appointment_Date = StringField('Appointment Date', validators=[DataRequired()])
    submit = SubmitField('Add appointment')
