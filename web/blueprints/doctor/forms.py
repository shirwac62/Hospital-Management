from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class DoctorForm(FlaskForm):
    doc_full_name = StringField('Doc Full Name', validators=[DataRequired(), Length(min=2, max=20)])
    doc_address = StringField('Doc Address', validators=[DataRequired()])
    doc_ph_no = IntegerField('Doc Ph No', validators=[DataRequired()])
    submit = SubmitField('Add Doctor')