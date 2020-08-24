import io
import csv
from flask_json import FlaskJSON, json_response, as_json
from flask import Flask
from flask import make_response
from flask import request
from flask import render_template, flash, redirect, url_for
from datetime import datetime
from flask import jsonify
from markupsafe import escape
import pytz


from config import Config
from forms import LoginForm, SingUpForm


app = Flask(__name__)
app.config.from_object(Config)
FlaskJSON(app)


@app.route("/")
@app.route("/index-url")
def index():
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
    # return f"Today is {date}"
    return render_template("date.html", **{"title": "My title", "date": datetime.today()})


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('.index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/sing_up', methods=['GET', 'POST'])
def sing_up():
    form = SingUpForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data))
        return redirect(url_for('timezones'))
    return render_template('sing_up.html', title='Sign Up', form=form)


@app.route('/json-response')
@as_json
def json_route():
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
    return posts


@app.route('/download')
def download_csv():
    io_file = io.StringIO()
    cw = csv.writer(io_file)
    csv_list = [
        ['id', 'name', 'email'],
        ['1', 'Vasile', 'vasile@gmail.com'],
        ['2', 'Ion', 'ion@gmail.com']
    ]
    cw.writerows(csv_list)
    output = make_response(io_file.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output
