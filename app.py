import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def cats():
    URL = 'https://api.thecatapi.com/v1/images/search'
    r = requests.get(URL)
    json = r.json()
    url = json[0]["url"]

    return "<img src = '" + url + "'></img>"








# --------------------------------------------

# import requests

# URL = 'https://api.thecatapi.com/v1/images/search'
# r = requests.get(URL)
# json = r.json()
# url = json[0]["url"]
# print(url)
