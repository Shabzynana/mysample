from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    # no empty titles or text possible
    # we'll grab the date automatically from the Model later
    text = TextAreaField('Comment', validators=[DataRequired(message='plesase input data')])
    submit = SubmitField('Comment')
