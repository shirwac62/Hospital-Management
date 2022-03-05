from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ProcedureForm(FlaskForm):
    procedure_id = StringField('Procedure ID', validators=[DataRequired(), Length(min=2, max=20)])
    procedure_code = StringField('Procedure code', validators=[DataRequired(), Length(min=2, max=20)])
    procedure_name = StringField('Procedure name', validators=[DataRequired()])
    cost = StringField('Cost', validators=[DataRequired()])

    submit = SubmitField('Add Nurse')
