# from flask import Flask
# from flask import render_template
# import random
# import datetime as dt
#
# app = Flask(__name__)
#
# @app.route("/")
# def home():
#     random_num = random.randint(0, 10)
#     current_year = dt.datetime.now().year
#
#     return render_template("index_2.html", num=random_num, year=current_year)
#
# if __name__ == "__main__":
#     app.run(debug=True)

# ===========================================================

import requests, json

# url_gender = "https://api.genderize.io?name="
# url_age = "https://api.agify.io/?name="
# name = "dima"
# print(name)
#
# url = requests.get(url=url_gender + name)
# data = json.loads(url.text)['gender']
# print(data)
#
# url = requests.get(url=url_age + name)
# data = json.loads(url.text)['age']
# print(data)

# url = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
# data = json.loads(url.text)
# for item in data:
#     print(item)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()
for item in all_posts:
    print(item)

print(all_posts[0]['title'])

# {% for i in range(11) %}
# {{ i }}
# {% endfor %}

