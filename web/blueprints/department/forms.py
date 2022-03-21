from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class departmentForm(FlaskForm):
    department_name = StringField('department name', validators=[DataRequired()])
    Head_id = StringField('Head ID', validators=[DataRequired()])
    head_name = StringField(' Head Name', validators=[DataRequired()])
    submit = SubmitField('Add Department')
