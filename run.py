import os #not sure what this is
from flask import Flask
from flask import request, redirect, url_for #added 2/5
from flask import render_template, jsonify
from flask_cors import CORS
from random import *
from werkzeug.utils import secure_filename   #2/5

UPLOAD_FOLDER = "uploads" #2/5
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']) #2/5

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  #2/5
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/random', methods=['GET'])
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/api/upload', methods=['GET','POST'])
def upload_me():
    print ("now in the route for api/upload")
    if request.method == 'GET':
       """ show the information"""
       import json
       print ("now in if GET")
       with open("foo.data", "rb") as f:
           string = f.read()
       object = json.loads(string.decode("utf-8"))
       return object["key"]
    if request.method == 'POST':
       """ return the information"""
       data = request.form
       print (type(data))
       print (request.get_data())
       with open("foo.data", "wb") as f:
           string = request.get_data()
           f.write(string)
       return jsonify (data["key"])
       return jsonify (data)
       

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

def index():
        return render_template("index.html")
