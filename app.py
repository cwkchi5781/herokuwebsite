from flask import Flask, render_template, request, jsonify, redirect, session, url_for
import gunicorn, mysql.connector
from datetime import datetime


app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("landing.html", page="home")

if __name__ == '__main__':
    app.run()