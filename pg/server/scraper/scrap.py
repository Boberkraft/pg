import bs4
from threading import get_ident
import re
from .form import Form
from .radio_form import RadioForm
from .true_false_form import TrueFalseForm
from .dropdowns_form import DropdownsForm
from .checkboxes_form import CheckboxesForm
from .table_form import TableForm
from time import sleep, time
from flask_sqlalchemy import SQLAlchemy
from pg.server.database import UnprocessedScrapedPage
from pg.server.database import db
from pg.server import app

SPACE_PATTERN = re.compile(r'\s{2,}')

types = [RadioForm, TrueFalseForm, DropdownsForm, CheckboxesForm, TableForm]


def process_pages_from_db():
    while True:
        with app.app_context():
            page = UnprocessedScrapedPage.query.first()
        if page:
            start = time()
            process_page(page)
            print("TOOK:", time() - start)
        else:
            print('Nothing found')
        sleep(4)

def process_page(page):
    process_html(page.html)
    # with app.app_context():
    #     db.session.delete(page)
    #     db.session.commit()

def process_html(html):
    soup = bs4.BeautifulSoup(remove_spaces(html), 'html.parser')
    process_page_soup(soup)


def remove_spaces(html):
    return SPACE_PATTERN.sub(' ', html)


def process_page_soup(soup):
    for form in Form.find_all(soup):
        if form.is_valid():
            for type in types:
                form = type(form._html)
                if type.is_in_type(form):
                    print(form.question_html())
                    print(f" - {type.__name__} is in type")
                    break
            else:
                print("NOT FOUND")
        else:
            print('NOT VALID NEXT')