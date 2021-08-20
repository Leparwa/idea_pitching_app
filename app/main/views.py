from flask.templating import render_template
from flask_login import login_required
from flask import render_template
from . import main

@main.route('/', methods = ['GET','POST'])
@login_required
def user_profile():
    return render_template('user_profile.html')