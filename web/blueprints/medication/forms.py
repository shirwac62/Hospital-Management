from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class MedicationForm(FlaskForm):
    code = StringField('code', validators=[DataRequired(), Length(min=2, max=20)])
    name = StringField('name', validators=[DataRequired(),  Length(min=2, max=20)])
    brand = StringField('brand', validators=[DataRequired(),  Length(min=2, max=20)])
    description = StringField('description', validators=[DataRequired(),  Length(min=2, max=20)])
    submit = SubmitField('Add Medication')
