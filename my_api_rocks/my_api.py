import sys

def q(text=''):
    print(f'>{text}<')
    sys.exit() 

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config['DEBUG'] = True

bois = [
    {
        'name' : 'sammy boy',
        'skill': 'can stick to a chair and study for hours during the exams'
    },
    {
        'name' : 'seth',
        'skill': 'manipulating people is as easy as ABC... ' 
    },
    {
        'name' : 'deepi',
        'skill': 'cant get high. but he will make sure that all his bois are flying high'
    }
]

@app.route('/', methods = ['GET'])
def home():
    # return jsonify(bois)
    return '<h1 style="color:MediumSeaGreen; background-color:#CCCCFF;">home page it is !</h1>'

@app.route('/bois', methods = ['GET'])
def bois_who():
    return jsonify(bois)

@app.route('/that_boi', methods = ['GET'])
def boi_with_a_name():
    if 'name' in request.args:
        name = request.args['name']
    else:
        return '<h2 style="background-color:FF0033;">whats the boi name ?</h2>'

    result = None
    for boi in bois:
        if boi['name'] == name:
            result = boi

    if result is not None:            
        return jsonify(result)
    else:
        return '<h3 style="background-color:powderblue;">wrong boi !</h3>'


app.run()
# app.run(host = '0.0.0.0', port = '5432') # to change the port