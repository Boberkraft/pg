import bs4
import re

from form import Form
from radio_form import RadioForm
from true_false_form import TrueFalseForm
from dropdowns_form import DropdownsForm
from checkboxes_form import CheckboxesForm
from table_form import TableForm
from .
with open('pytania.html', encoding='utf-8') as f:
    p = re.compile(r'\s{2,}')
    plik = p.sub(' ', f.read())

soup = bs4.BeautifulSoup(plik, 'html.parser')


types = [RadioForm, TrueFalseForm, DropdownsForm, CheckboxesForm, TableForm]

def process_pages():


def process_soup(html):
    for form in Form.find_all(html):
        if form.is_valid():
            print()
            print()
            for type in types:
                if type.is_in_type(form):
                    print(f"{type.__name__} is in type")
                    break
            else:
                # exceptionp

                print(form.html())
                print("NOT FOUND")
                print()
                print()
        else:
            print('NOT VALID NEXT')

