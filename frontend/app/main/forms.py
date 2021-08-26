from logging import PlaceHolder
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField, SelectField
from wtforms.fields.simple import FileField
from wtforms.validators import Required

pitch_categories = [('--Select--'),('Environment'), ('Health'), ('Education'), ('Business')]
class PitchForm(FlaskForm):
    title = StringField('Title',validators=[Required()])

    category = SelectField('Category', choices=pitch_categories, validators=[Required()])

    pitchSummary = StringField('Problem you are solving')

    pitchDesc = TextAreaField('Describe Your Idea')

    image = FileField('Image')

    submit = SubmitField('Submit')