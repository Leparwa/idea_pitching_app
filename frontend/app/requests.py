import urllib.request,json
from .models import Pitch

def configure_request(app):
    global apiKey,base_url
    base_url = app.config['PITCHES_API_BASE_URL']


def get_pitches(endpoint):
    '''
    Function that gets the json response to our url request
    '''
    get_pitches_url = base_url.format(endpoint)
    with urllib.request.urlopen(get_pitches_url) as url:
        get_data = url.read()
        response = json.loads(get_data)
        if response['data']:
            # results_list = response['data']
            results = response['data']
           
            # results = process_pitches(results_list)  
    return results

def process_pitches(pitches):
    processed_data = []
    for pitch in pitches:
        title = pitch.get('title')
        image = pitch.get('image')
        pitchDesc = pitch.get('pitchDesc')
        category = pitch.get('category')
        user_id = pitch.get('user_id')
        pitchSummary = pitch.get('pitchSummary')
        print(title)
        pitch_object = Pitch(title, image, pitchDesc, category, user_id, pitchSummary)
        processed_data.append(pitch_object)
    return processed_data
