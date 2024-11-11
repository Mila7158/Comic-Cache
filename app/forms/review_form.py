from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class ReviewForm(FlaskForm):
    review = TextAreaField("Review", validators=[DataRequired()])
    stars = IntegerField("Stars", validators=[DataRequired(), NumberRange(min=1, max=5)])