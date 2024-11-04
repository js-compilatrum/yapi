from flask import Flask
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return f'Hello World! now {datetime.now()}'


if __name__ == '__main__':
    app.run()
