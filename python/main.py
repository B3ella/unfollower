from instagram_private_api import Client
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/login")
def handle_login():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return "<p>content type not suported</p>"
    username = request.json.get("username")
    password = request.json.get("password")
    print(username, password)


def login(username: str, password: str) -> Client:
    return Client(username, password)
