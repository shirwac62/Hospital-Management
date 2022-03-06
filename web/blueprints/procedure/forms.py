from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class ProcedureForm(FlaskForm):
    procedure_code = IntegerField('Procedure Code', validators=[DataRequired()])
    procedure_name = StringField('Procedure Name', validators=[DataRequired(), Length(min=2, max=6)])
    cost = StringField('Cost', validators=[DataRequired()])
    submit = SubmitField('Add Procedure')