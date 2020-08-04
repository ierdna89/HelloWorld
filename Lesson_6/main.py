from flask_json import FlaskJSON, json_response, as_json
from flask import Flask
from markupsafe import escape
from flask import request
from flask import render_template
from datetime import datetime
from flask import jsonify
import pytz

from config import Config


app = Flask(__name__)
# app.config.from_ojects(Config)


@app.route("/")
@app.route("/index")
def index():
    return "Hello world"


@app.route("/user/<name>/<last_name>/")
def show_profile_username(name, last_name):
    return f"Hello {escape(name)}, {escape(last_name)}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f"Post {post_id}"


@app.route("/search")
def show_query_params():
    searchword = request.args.get("key")
    return f"You are looking for {escape(searchword)}"


@app.route("/date/")
def show_date():
    date = datetime.today()
    return f"Today is {date}"


@app.route("/template")
def template_route():
    user = {"username": "Andrei"}
    posts = [
        {
            'author': {'username': 'Vasile'},
            'body': 'Beautiful day in Chisinau!'
        },
        {
            'author': {'username': 'Ion'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template("index.html", **{"title": "My title", "user": user, "posts": posts})


@app.route("/timezones/")
def timezones():

    time_Chisinau = datetime.now(pytz.timezone('Europe/Bucharest'))
    time_London = datetime.now(pytz.timezone('Europe/London'))
    time_NY = datetime.now(pytz.timezone('US/Eastern'))

    return render_template("timezones.html", **{"title": "My title", "time_Chisinau": time_Chisinau.strftime("%H:%M"), "time_NY": time_NY.strftime("%H:%M"), "time_London": time_London.strftime("%H:%M")})


@app.route("/your_ip/", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200
