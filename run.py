import base64
import os #not sure what this is

from flask import Flask
from flask import Response
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
       print ("now in if GET")
       with open("foo.image", "rb") as f:
           data = f.read().decode("utf-8")
           data = data[len("data:"):]  # strip off "data:"
           header, data = data.split(",",1)
           mimetype = header.split(";")[0]
           return Response(base64.b64decode(data), mimetype=mimetype)
       with open("foo.name", "rb") as f:
           return f.read()
    if request.method == 'POST':
       """ return the information"""
       import json
       data = json.loads(request.get_data().decode("ascii"))
       print (type(data))
       print (request.get_data())
       with open("foo.image", "wb") as img:
           img.write(data["data"].encode("utf-8"))
       with open("foo.name", "wb") as f:
           f.write(data["name"].encode("utf-8"))
       return jsonify (data)
       

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

def index():
        return render_template("index.html")
