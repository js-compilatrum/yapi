from datetime import datetime

from flask import Flask
import requests
import lxml
from bs4 import BeautifulSoup as soup

""" Simple Flask application """
app = Flask(__name__)

happy_smiley_b64 = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAnXAAAJ1wGxbhe3AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAgZJREFUOI2lkj9oU2EUxX/3S4JNWqsJBaGIBWnpkkShk7o1RXAICE0KLmIL0kUQ6ebs4CRFXYpRiw5iXjOJOPhncSgOYkgr2KaiQnGQQkL/5KVp37sOyYtpiFPvdi7nnu/cez44ZEmnZv9IMlTZ6xozyiCIuqLfQ4Hqu9+fX1Xaub52wUg0NbPnBHLAKQVboRdI7jv+u6ET0X37z9dP/3Mg4djEc1QHHL87tZnPFVuJvWfHh3yueYrqj9LSwlVADwhEoqkZRS6XqttjrL3Z7bjw4KUj4WDPBxW1yoWF2aZA/0gyZO92/XL87vnNfK6YntMYgDUtSwCtuC+eHnaUj909DKwvWrYBsPeCCRW+eLbVkFRD0nu4FW8UrBWBws4WowB+AHEZBvLeQI+fe63O27ErkjfoMPDaNFqqRoxHqNkE5yel6uH5SanWbIJNBVUBUQBTt2hWUY0DpDMaqQVYST/SUY+fymiiFuBbOqORxtAZVV09eMRa10/H517YzOeKqcd6EeUhyjHqeZUN3LCuy9v2I/6LMTZxS0XHS5XthBfjlTntA3gxLRsHYlR5WV7O3m86aJSEY6lnIKd9wtRGwVppPVzj5SeorJWWs9do/0ieyPF46qao3BYouGihvrPEFeKqcqe8nH3gDXcSAODkuXRwZ0sTImaofnS32H1U3q8vWnYn/qHqL8V35T417C5JAAAAAElFTkSuQmCC"
smiley_img = f'<img src="{happy_smiley_b64}">'
def parse_lord_words(html_source: str) -> dict:
    if not isinstance(html_source, str):
        return {'error': 'source is not a string'}

    data = soup(html_source, 'lxml')
    div = data.find_all('div', class_='ewangelia')
    bible_quote = ''.join([result.text for result in div])

    if bible_quote:
        return {'bible': bible_quote}
    return {'bible': "?"}


@app.route('/')
def hello_world():  # put application's code here
    curr_datetime = datetime.now()
    hour = curr_datetime.hour
    minut = curr_datetime.minute
    second = curr_datetime.second
    year = curr_datetime.year
    month = curr_datetime.month
    day = curr_datetime.day

    nowis = f"{year}.{month}.{day} {hour}:{minut}.{second}<br><br>"
    progress = "<br>" + "_" * 10 + "<br>"
    progress += f"{month} {str(smiley_img * month)}<br>"
    progress += f"{day} {str(smiley_img * day)}<br>"
    progress += "<hr>"
    progress += f"{hour} {str(smiley_img * hour)}<br>"
    progress += f"{minut} {str(smiley_img * minut)}<br>"
    progress += f"{second} {str(smiley_img * second)}<br>"

    text = f"{nowis}{progress}"

    return f'On world<br><hr>{text}'


@app.route('/bible')
def bible_words():
    html = requests.get('https://opoka.org.pl/liturgia/')
    return html.text


@app.route('/bible/words')
def show_bible_quote():
    html = requests.get('https://opoka.org.pl/liturgia/')
    if html.text and html.text != "":
        return parse_lord_words(html.text)
    return {'error': 'No source available'}


if __name__ == '__main__':
    app.run()
