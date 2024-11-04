from datetime import datetime

from flask import Flask
import requests
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return f'Hello World! now {datetime.now()}'

@app.route('/bible')
def bible_words():
    html = requests.get('https://opoka.org.pl/liturgia/')
    return html.text

if __name__ == '__main__':
    app.run()
