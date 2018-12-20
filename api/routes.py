from flask import Flask, jsonify, request, make_response


app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"message":"Hello World"}),200