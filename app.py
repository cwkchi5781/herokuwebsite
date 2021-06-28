from engineio.async_drivers import eventlet
from flask import Flask, render_template, request, jsonify, redirect, session, url_for
from flask_socketio import SocketIO, emit
import gunicorn, mysql.connector
from datetime import datetime
import gevent
import gevent_websocket



app = Flask(__name__)
#mysql://b0ccf8cd5f7945:27fb9f4e@us-cdbr-east-04.cleardb.com/heroku_bde763ff3f353c6?reconnect=true

db = mysql.connector.connect(
    host="us-cdbr-east-04.cleardb.com",
    user="b0ccf8cd5f7945",
    password="27fb9f4e",
    database="heroku_bde763ff3f353c6")

cursor = db.cursor()

app.config['SECRET_KEY'] = 'dfgdfgdf'
socketio = SocketIO(app)
#socketio.init_app(app, cors_allowed_origins=["https://portfolio2004.herokuapp.com/"])

#hi

cursor.execute("CREATE TABLE IF NOT EXISTS enteries (id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50), text VARCHAR(100))")



@app.route('/', methods=["POST", "GET"])
def index():
    print("hi")
    return render_template("landing.html", page="home")

@socketio.on('sendusername')
def sendusername(data):
    print("server recieve")
    sql = "SELECT * FROM enteries WHERE username=%s"
    username = (str(data['username']),)
    cursor.execute(sql, username)
    usernamestatus = cursor.fetchall()
    if usernamestatus == []:
        usernamestatus = True
    else:
        usernamestatus = False

    emit('comfirmusername', usernamestatus)

if __name__ == '__main__':
    socketio.run()