from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

class RatingForm(FlaskForm):
    rating = RadioField("Rating", choices=[1,2,3,4,5],validators=[DataRequired()])
    submit = SubmitField("Next")