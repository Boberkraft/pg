from form import Form
from true_false_form import TrueFalseForm
import re

class RadioForm(Form):
    @staticmethod
    def is_in_type(form):
        return all([
            TrueFalseForm.asks_for_one_answer(form),
            RadioForm.contains_radios(form)
        ])

    @staticmethod
    def contains_radios(form):
        # 2 radios are for TrueFalseForm
        return len(form.html().find_all('input')) > 2

