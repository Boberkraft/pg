from form import Form
import re

class TableForm(Form):
    @staticmethod
    def is_in_type(form):
        return all([
            TableForm.has_class_multianswer(form),
            TableForm.has_some_selects(form)
        ])

    @staticmethod
    def has_class_multianswer(form):
        return 'match' in form.html().get('class')

    @staticmethod
    def has_some_selects(form):
        return len(form.html().find_all('select')) > 0
