from flask import Flask, render_template, request, jsonify, redirect, session, url_for
import gunicorn, mysql.connector
from datetime import datetime


app = Flask(__name__)
#mysql://b0ccf8cd5f7945:27fb9f4e@us-cdbr-east-04.cleardb.com/heroku_bde763ff3f353c6?reconnect=true

db = mysql.connector.connect(
    host="cdbr-east-04.cleardb.com",
    user="b0ccf8cd5f7945",
    password="27fb9f4e",
    database="heroku_bde763ff3f353c6")

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("landing.html", page="home")

if __name__ == '__main__':
    app.run()