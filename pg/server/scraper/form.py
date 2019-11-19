import bs4
import re

class Form:
    @staticmethod
    def find_all(soup):
        x = []
        for d in soup.find_all('div', id=re.compile(r'^question-\d+-\d+$')):
            x.append(Form(d))
        return x

    def __init__(self, html):
        self._html = html

    def is_valid(self):
        return None not in [self.html()]

    def html(self):
        return self._html

    def parent_id(self):
        return self.html().get('id').split('-')[1]

    def id(self):
        return self.html().get('id').split('-')[2]

    def question_html(self):
        return self.html().find('div', class_='qtext')

    def question(self):
        raw = self.question_html()
        if raw:
            return ''.join(raw.strings)

    def answer_html(self):
        return self.html().find('div', class_='ablock')