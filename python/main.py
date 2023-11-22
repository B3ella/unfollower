from instagram_private_api import Client
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def login(username: str, password: str) -> Client:
    return Client(username, password)
