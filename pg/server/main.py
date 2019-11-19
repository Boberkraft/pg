import sys
sys.path.append('./..')
from flask import Flask
from flask import jsonify
from flask import request
from random import randint
from threading import Thread
from scraper.scrap import process_pages_from_db
from pg.server import app, db
from pg.server.database import UnprocessedScrapedPage

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
    Thread(target=process_pages_from_db).start()
    app.run(debug=False)
