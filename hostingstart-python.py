from flask import Flask, jsonify,render_template, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello():
    return render_template('hostingstart-python.html')
