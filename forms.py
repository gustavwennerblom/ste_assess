from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.widgets import ListWidget
from wtforms.validators import InputRequired
import csv


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
    choices = [('Ja', 'Ja'), ('Delvis', 'Delvis'), ('Nej', 'Nej')]
    q1 = RadioField(label=questions.get('q1'), choices=choices,
                    validators=[InputRequired(message="Frågan saknar svar")])
    q2 = RadioField(label=questions.get('q2'), choices=choices,
                    validators=[InputRequired(message="Frågan saknar svar")])
    q3 = RadioField(label=questions.get('q3'), choices=choices,
                    validators=[InputRequired(message="Frågan saknar svar")])
    q4 = RadioField(label=questions.get('q4'), choices=choices,
                    validators=[InputRequired(message="Frågan saknar svar")])
    q5 = RadioField(label=questions.get('q5'), choices=choices,
                    validators=[InputRequired(message="Frågan saknar svar")])
    q6 = RadioField(label=questions.get('q6'), choices=choices,
                    validators=[InputRequired(message="Frågan saknar svar")])
    q7 = RadioField(label=questions.get('q7'), choices=choices,
                    validators=[InputRequired(message="Frågan saknar svar")])
    q8 = RadioField(label=questions.get('q8'), choices=choices,
                    validators=[InputRequired(message="Frågan saknar svar")])
    q9 = RadioField(label=questions.get('q9'), choices=choices,
                    validators=[InputRequired(message="Frågan saknar svar")])
    q10 = RadioField(label=questions.get('q10'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    q11 = RadioField(label=questions.get('q11'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    q12 = RadioField(label=questions.get('q12'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    q13 = RadioField(label=questions.get('q13'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    q14 = RadioField(label=questions.get('q14'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    q15 = RadioField(label=questions.get('q15'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    q16 = RadioField(label=questions.get('q16'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    q17 = RadioField(label=questions.get('q17'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    q18 = RadioField(label=questions.get('q18'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    q19 = RadioField(label=questions.get('q19'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    q20 = RadioField(label=questions.get('q20'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    q21 = RadioField(label=questions.get('q21'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    q22 = RadioField(label=questions.get('q22'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    q23 = RadioField(label=questions.get('q23'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    q24 = RadioField(label=questions.get('q24'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    q25 = RadioField(label=questions.get('q25'), choices=choices,
                     validators=[InputRequired(message="Frågan saknar svar")])
    submit = SubmitField(label="Skicka svar")
