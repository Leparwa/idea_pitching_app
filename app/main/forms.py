from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField
from wtforms.fields.simple import FileField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Title',validators=[Required()])
    pitch_desc = TextAreaField('Describe Your Idea')
    pitch_image_path = FileField()
    submit = SubmitField('Submit')