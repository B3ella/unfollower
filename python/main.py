from instagram_private_api import Client
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/login", methods=['POST'])
def handle_login():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username, password)
    return username


def login(username: str, password: str) -> Client:
    return Client(username, password)
