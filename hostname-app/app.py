import socket

from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_host():
    return f"{socket.gethostname()} - V1"
