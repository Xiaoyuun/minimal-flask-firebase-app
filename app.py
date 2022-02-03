from flask import Flask, request
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)
cred = credentials.Certificate(
    'credentials.json')
initialize_app(cred)
db = firestore.client()

@app.route("/", methods=["POST", "GET"])
def base():
    return "API works"

@app.route("/icecream", methods=["POST", "GET"])
def icecream():
    return "chocolate icecream is superior"

@app.route("/fetchAvenu", methods=["POST", "GET"])
def fire_route():
    doc = db.collection(u'events').document(
        u'09hQ1TqJgZg9Ary01xmKR89Z5W1y').get()
    return doc.to_dict()


@app.route("/createCol", methods=["POST", "GET"])
def create_col():
    db.collection("new-coll").add({"Hello": "World"})
    return "created"