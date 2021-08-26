from flask import request, jsonify, make_response
from models import Pitch, PitchSchema
from . import main
from app_api import db
@main.route('/pitch', methods=['POST'])
def create_pitch():
    data = request.get_json()
    pitches_schema = PitchSchema()
    pitch = pitches_schema.load(data)
    result = pitches_schema.dump(pitch.create())
    return make_response(jsonify({"data": result}), 200)
  
@main.route('/pitch', methods=['GET'])
def get_all_pitches():
    pitches_schema = PitchSchema(many=True)
    all_pitches = Pitch.query.all()
    result = pitches_schema.dump(all_pitches)
    return make_response(jsonify({"data": result}))

@main.route('/pitch/<id>', methods=['GET'])
def get_pitch_by_id(id):
   get_pitch = Pitch.query.get(id)
   pitch_schema = PitchSchema()
   pitch = pitch_schema.dump(get_pitch)
   return make_response(jsonify({"todo": pitch}))

@main.route('/pitch/<id>', methods=['DELETE'])
def delete_pitch_by_id(id):
   get_pitch = Pitch.query.get(id)
   db.session.delete(get_pitch)
   db.session.commit()
   return make_response("", 204)
