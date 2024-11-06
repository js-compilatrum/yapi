from datetime import datetime

from flask import Flask
import requests
import lxml
from bs4 import BeautifulSoup as soup

""" Simple Flask application """
app = Flask(__name__)


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
    return f'Hello World! now <{datetime.now()}>'


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
