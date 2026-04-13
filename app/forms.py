from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField, SelectField, IntegerField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange

class MovieForm(FlaskForm):
  title = StringField('Title', validators=[DataRequired(message="Title is required"), Length(max=100, message="Title must be less than 100 characters")])
  description = TextAreaField('Description', validators=[DataRequired(message="Description is required"), Length(max=1000, message="Description must be less than 1000 characters")])
  poster = FileField('Poster', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
  submit = SubmitField('Add Movie')