from flask_login import login_required
from . import main

@main.route('/pitches/review/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    pass