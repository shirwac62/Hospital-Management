from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class DoctorForm(FlaskForm):
    doc_full_name = StringField('doc_full_name', validators=[DataRequired(), Length(min=2, max=20)])
    doc_address = StringField('doc_address', validators=[DataRequired()])
    doc_ph_no = IntegerField('doc_ph_no', validators=[DataRequired()])
    submit = SubmitField('Add Doctor')