from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.widgets import ListWidget
import csv
from collections import OrderedDict

class MaterializeListWidget(ListWidget):
    def __init__(self):
        super(MaterializeListWidget, self).__init__()

    def __call__(self, field, **kwargs):
        return super(MaterializeListWidget, self).__call__(field, **kwargs)

def get_questions():
    questions = {}
    options = {}
    with open('questions.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for line in reader:
            questions[line['Number']] = line['QuestionText']
    return questions, options


class MainQuestionnaire(FlaskForm):
    questions, options = get_questions()
    choices = [('Ja','Ja'), ('Delvis','Delvis'), ('Nej','Nej')]
    q1 = RadioField(label=questions.get('q1'), choices=choices)
    q2 = RadioField(label=questions.get('q2'), choices=choices)
    q3 = RadioField(label=questions.get('q3'), choices=choices)
    q4 = RadioField(label=questions.get('q4'), choices=choices)
    q5 = RadioField(label=questions.get('q5'), choices=choices)
    q6 = RadioField(label=questions.get('q6'), choices=choices)
    q7 = RadioField(label=questions.get('q7'), choices=choices)
    q8 = RadioField(label=questions.get('q8'), choices=choices)
    q9 = RadioField(label=questions.get('q9'), choices=choices)
    q10 = RadioField(label=questions.get('q10'), choices=choices)
    q11 = RadioField(label=questions.get('q11'), choices=choices)
    q12 = RadioField(label=questions.get('q12'), choices=choices)
    q13 = RadioField(label=questions.get('q13'), choices=choices)
    q14 = RadioField(label=questions.get('q14'), choices=choices)
    q15 = RadioField(label=questions.get('q15'), choices=choices)
    q16 = RadioField(label=questions.get('q16'), choices=choices)
    q17 = RadioField(label=questions.get('q17'), choices=choices)
    q18 = RadioField(label=questions.get('q18'), choices=choices)
    q19 = RadioField(label=questions.get('q19'), choices=choices)
    q20 = RadioField(label=questions.get('q20'), choices=choices)
    q21 = RadioField(label=questions.get('q21'), choices=choices)
    q22 = RadioField(label=questions.get('q22'), choices=choices)
    q23 = RadioField(label=questions.get('q23'), choices=choices)
    q24 = RadioField(label=questions.get('q24'), choices=choices)
    q25 = RadioField(label=questions.get('q25'), choices=choices)
    submit = SubmitField(label="Skicka svar")
