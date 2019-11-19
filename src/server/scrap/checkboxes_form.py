from form import Form
import re

class CheckboxesForm(Form):
    @staticmethod
    def is_in_type(form):
        return all([
            CheckboxesForm.asks_for_multiple_answers(form)
        ])

    @staticmethod
    def asks_for_multiple_answers(form):
        return bool(form.answer_html().find_all(text='Wybierz jedną lub więcej:'))
