from .form import Form
import re


class DropdownsForm(Form):
    def question_html(self):
        self.html()
        # TODO: TUTAJ HE!
        self.html().find('div', class_='formulation clearfix').find('p')

    @staticmethod
    def is_in_type(form):
        return all([
            DropdownsForm.has_class_multianswer(form),
            DropdownsForm.has_some_selects(form)
        ])

    @staticmethod
    def has_class_multianswer(form):
        return 'multianswer' in form.html().get('class')

    @staticmethod
    def has_some_selects(form):
        return len(form.html().find_all('select')) > 0
