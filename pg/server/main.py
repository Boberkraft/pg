from flask import Flask
from flask import jsonify
from flask import request
from database import db, show, UnprocessedScrapedPage
from random import randint
from threading import Thread
from scraper import scrap
DATABASE_PATH = 'test.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DATABASE_PATH}"


def nice_s(s):
    SIZE = 15
    if len(s) > SIZE:
        return s[:SIZE] + '...'
    else:
        return s + '...'


@app.route('/send', methods=['POST'])
def send_data():
    data = request.get_json()

    print("New data!")
    print(nice_s(data['html']))

    queue_page(data['html'] + str(randint(0, 9)))

    return jsonify(html=nice_s(data['html']))


def queue_page(html):
    raw_page = UnprocessedScrapedPage(html=html)
    db.session.add(raw_page)
    db.session.commit()
    # show()


if __name__ == '__main__':
    db.init_app(app)
    Thread(target=)
    app.run(debug=True)
