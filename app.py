# python -m flask run
from flask import Flask, render_template, redirect, request, session, jsonify, flash
from flask_login import logout_user
from flask_session import Session
from flask_socketio import SocketIO, join_room, leave_room, emit
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
socketio = SocketIO(app)
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Responses arent chached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response 

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route("/")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    socketio.run(app, host="localhost", debug=True)

