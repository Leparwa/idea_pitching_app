from sys import flags
from flask import  render_template, redirect, url_for, session, jsonify
from flask.helpers import flash
from flask_login import login_required, current_user
from flask_login.mixins import AnonymousUserMixin
from . import main
from werkzeug.utils import secure_filename
from ..models import Pitch
from  ..requests import get_pitches
from .forms import PitchForm
import os



@main.route('/', methods = ['GET','POST'])
@login_required
def user_profile():
    return render_template('user_profile.html')

@main.route('/new-pitch', methods = ['POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        uploaded_file = form.image.data
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
      
            uploaded_file.save(os.path.join('app/static/photos', filename))
     
        path = f'../static/photos/{filename}'
        print(current_user.id)
        user_id = current_user.id
        new_pitch = Pitch(title=form.title.data, image=path, pitchDesc=form.pitchDesc.data, pitchSummary=form.pitchSummary.data, user_id=user_id, category=form.category.data)
      
        # save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.new_pitch'))

    return render_template('new_pitch.html', new_pitch_form=form)

@main.route('/all-pitches', methods = ['GET'])
def get_all_pitches():
    pitch_data = get_pitches('/pitch')
  
    return render_template('all_pitches.html', pitches = pitch_data) 




