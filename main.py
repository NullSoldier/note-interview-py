from flask import Flask, jsonify, request, abort, make_response
from database import Database, Note

app = Flask(__name__)

@app.get("/")
def say_hello_world():
    return make_response(jsonify({"hello": "world"}), 200)
