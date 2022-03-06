from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Length


class RoomForm(FlaskForm):
    room_no = IntegerField('Room No', validators=[DataRequired()])
    room_type = StringField('Room Type', validators=[DataRequired(), Length(min=2, max=20)])
    available = StringField('Available', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Add Room')