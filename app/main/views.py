from os import abort
from urllib import request
from flask.templating import render_template
from flask import config, render_template, redirect, url_for
from flask_login import login_required, current_user
from . import main
from werkzeug.utils import secure_filename
from ..models import Pitch
from .forms import PitchForm
import markdown2
from .. import app
import os

from app.main import forms 
@main.route('/', methods = ['GET','POST'])
@login_required
def user_profile():
    return render_template('user_profile.html')

@main.route('/pitch', methods = ['GET','POST'])
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        uploaded_file = form.pitch_image_path.data
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
      
            uploaded_file.save(os.path.join('app/static/photos', filename))
     
        path = f'app/static/photos/{filename}'
        print(path)
        new_pitch = Pitch( pitch_title=form.title.data, pitch_image_path=path, pitch_desc=form.pitch_desc.data)

        # save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.new_pitch'))

    return render_template('new_pitch.html', new_pitch_form=form)

@main.route('/review/<int:id>')
def single_review(id):
    review=Pitch.query.get(id)
    # if review is None:
    #     abort()
    format_review = markdown2.markdown(review.pitch_desc,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('pitch_review.html',review = review,format_review=format_review)

