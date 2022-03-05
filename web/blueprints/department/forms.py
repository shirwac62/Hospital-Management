from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class departmentForm(FlaskForm):
    department_id = IntegerField(' department id ', validators=[DataRequired(), Length(min=2, max=20)])
    department_name = StringField('department name', validators=[DataRequired()])
    Head_id = StringField('Head ID', validators=[DataRequired()])
    First_name = StringField(' First name', validators=[DataRequired()])
    Last_name = StringField('Lastname', validators=[DataRequired()])
    submit = SubmitField('Add department')
