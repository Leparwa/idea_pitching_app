from flask_login import login_required
from . import main

@main.route('/', methods = ['GET','POST'])
@login_required
def new_review():
    pass