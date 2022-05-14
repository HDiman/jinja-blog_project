from flask import Flask
from flask import render_template
import random
import datetime as dt

app = Flask(__name__)

@app.route("/")
def home():
    random_num = random.randint(0, 10)
    current_year = dt.datetime.now().year

    return render_template("index.html", num=random_num, year=current_year)

if __name__ == "__main__":
    app.run(debug=True)
