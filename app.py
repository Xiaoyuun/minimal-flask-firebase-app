from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def base():
    return "API works"

@app.route("/icecream", methods=["POST", "GET"])
def icecream(event_id):
    return "chocolate icecream is superior"
