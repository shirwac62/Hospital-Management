from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class NurseForm(FlaskForm):
    nurse_first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=20)])
    nurse_last_name = StringField('Last Name', validators=[DataRequired()])
    nurse_address = StringField('Address', validators=[DataRequired()])
    nurse_ph_no = IntegerField('Phone No', validators=[DataRequired()])
    submit = SubmitField('Add Nurse')
