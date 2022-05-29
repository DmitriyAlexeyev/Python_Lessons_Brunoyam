from bs4 import BeautifulSoup
import requests
from flask import Flask
import json


app = Flask(__name__)


# page = requests.get("https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D"
#                     "0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5")
#
# soup = BeautifulSoup(page.text, "html.parser")
#
# result = soup.find('div', {'class': 'ArchiveTemp'}).find('span', {'class': 't_0'})
#
# print(result.text)
#
# page = requests.get("http://127.0.0.1:5000/weather")
# print(page.text)


@app.route("/weather_api")
def weather_api():
    return json.dumps({"weather": 15})
