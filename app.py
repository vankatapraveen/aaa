
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Finance Portal is running!"


@app.route("/health")
def health():
    return {"status": "healthy"}
