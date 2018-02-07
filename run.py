import base64
import random # Avoid * imports as they add a lot of unkwnown namespaces to your file
import json
from flask import Flask, Response, request, redirect, url_for, render_template, jsonify
from flask_cors import cross_origin

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")


@app.route('/api/random', methods=['GET'])
def random_number():
    response = {'randomNumber': random.randint(1, 100)}
    return jsonify(response)


@app.route('/api/upload', methods=['GET','POST'])
@cross_origin(allow_headers=['Content-Type'])
def upload_me():
    if request.method == 'GET':
        """ Show image if already uploaded """
        print(request.files)
        return render_template('index.html')
    if request.method == 'POST':
       """ return the information"""
       data = json.loads(request.get_data().decode("ascii"))
       print(type(data))
       print(request.get_data())
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
