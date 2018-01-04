from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
import csv
from collections import OrderedDict

def get_questions():
    questions = {}
    options = {}
    with open('questions.csv', 'r') as f:
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
    submit = SubmitField(label="Skicka svar")

