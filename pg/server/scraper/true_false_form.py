from .form import Form


class TrueFalseForm(Form):
    @staticmethod
    def is_in_type(form):
        return all([
            TrueFalseForm.asks_for_one_answer(form),
            TrueFalseForm.contains_2_radios(form)
        ])

    @staticmethod
    def asks_for_one_answer(form):
        return 'wybierz jedną' in str(form.html().find('div', class_='prompt')).lower()

    @staticmethod
    def contains_2_radios(form):
        return len(form.html().find_all('input')) == 2
