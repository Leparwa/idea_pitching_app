from app_api import db, ma
from datetime import datetime

class Pitch(db.Model):
    __tablename__ = 'user_pitches'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200))
    image = db.Column(db.String)
    category = db.Column(db.String)
    pitchDesc = db.Column(db.String)
    pitchSummary = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users_table.id"))

    def __init__(self,  title, image, category, pitchDesc, user_id, pitchSummary):
        self.category =category,
        self.image = image
        self.pitchDesc = pitchDesc
        self.title = title
        self.user_id = user_id
        self.pitchSummary = pitchSummary

    def create(self):
       db.session.add(self)
       db.session.commit()
       return self
    
    def __repr__(self):
       return f"{self.id}"


class PitchSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'image', 'category', 'pitchDesc', 'pitchSummary', 'posted', 'user_id')