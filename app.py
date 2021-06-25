from flask import Flask, render_template, request, jsonify, redirect, session, url_for
import gunicorn, mysql.connector
from datetime import datetime


app = Flask(__name__)
#mysql://b0ccf8cd5f7945:27fb9f4e@us-cdbr-east-04.cleardb.com/heroku_bde763ff3f353c6?reconnect=true

db = mysql.connector.connect(
    host="us-cdbr-east-04.cleardb.com",
    user="b0ccf8cd5f7945",
    password="27fb9f4e",
    database="heroku_bde763ff3f353c6")

@app.route('/', methods=["POST", "GET"])
def index():
    return render_template("landing.html", page="home")

@app.route('/getuserip', methods=["POST", "GET"])
def userip():
    ip = request.environ['REMOTE_ADDR']
    print(ip)
    return render_template("landing.html", page="home", ip=ip)

if __name__ == '__main__':
    app.run()