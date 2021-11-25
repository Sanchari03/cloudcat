from flask import Flask, jsonify, request
import json

from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def home():
    render_template('page.html',template_folder='templates')

@app.route('/getstring', methods=['GET'])
def getLoan():
    inputString = request.args.get('palindrome')
    revString = inputString[::-1]
    if(revString == inputString):
        return jsonify({'message': f'{inputString} is a palindrome.'})
    else:
        return jsonify({'message': f'{inputString} is not a palindrome.'})

if __name__=='main':
    app.run()