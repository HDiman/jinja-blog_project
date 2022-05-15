from flask import Flask
from flask import render_template
import requests, json
import random
import datetime as dt

app = Flask(__name__)
url_gender = "https://api.genderize.io?name="
url_age = "https://api.agify.io/?name="

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guess/<name>")
def guess(name):
    url = requests.get(url=url_gender + name)
    gender = json.loads(url.text)['gender']
    url = requests.get(url=url_age + name)
    age = json.loads(url.text)['age']
    name = name.title()

    return render_template("guess.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
