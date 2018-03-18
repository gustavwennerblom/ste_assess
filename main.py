from flask import Flask, render_template, url_for, redirect, make_response, request, flash
from forms import MainQuestionnaire
import csv
import json
from keygen import get_secret_key
from config import DevConfig, PilotConfig, ProdConfig

app = Flask(__name__)
app.secret_key = get_secret_key(12)
app.config.from_object(PilotConfig)


@app.route('/')
def index():
    # return render_template('index.html')
    return redirect(url_for('assessment'))


@app.errorhandler(500)
def error_500(error):
    return render_template('500.html')


@app.route('/assessment', methods=['GET', 'POST'])
def assessment():
    form = MainQuestionnaire()
    if form.validate_on_submit():
        answers = {}
        for field in form:
            # Process question fields (discarding submit and csrf)
            if field.id.startswith("q"):
                answers[field.id] = field.data
        answers_json = json.dumps(answers)

        recommended_modules = recommend_modules(answers)
        feedback = generate_feedback(recommended_modules)

        resp = make_response(render_template('feedback.html', feedback=feedback))
        seconds_valid = 60 * 60 * 24 * 365  # One year in seconds
        resp.set_cookie('last_answer', value=answers_json, max_age=seconds_valid)
        return resp

    if request.cookies.get('last_answer'):
        #flash('Du verkar ha svarat tidigare. <a href="{{url_for("reload_feedback")}}">Klicka här </a> för att ladda om rekommendationen</a>')
        flash(render_template('reload_flash.html'))

    return render_template('assessment.html', form=form)


@app.route('/check_cookie')
def check_cookie():
    last_answer = request.cookies.get('last_answer')
    return("Last answer was {}".format(last_answer))


@app.route('/reload_feedback')
def reload_feedback():
    last_answer = json.loads(request.cookies.get('last_answer'))
    if not last_answer:
        flash("Failed to load previous answer")
        return redirect(url_for('assessment'))
    answers = json.loads(request.cookies.get('last_answer'))
    recommended_modules = recommend_modules(answers)
    feedback = generate_feedback(recommended_modules)
    return render_template('feedback.html', feedback=feedback)


def recommend_modules(answers):
    """
    :param answers: Dictionary of answers given
    :return: List of modules recommended
    """

    # Create a map of which question targets which module
    question_module_map = {}
    with open('questions.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for line in reader:
            question_module_map[line.get('Number')] = line['Module']

    # Check the answers and identify the suitable modules
    # Always recommend module 14
    recommended_modules = ['14']
    for question_number in answers:
        if not answers[question_number] == 'Ja':
            recommended_modules.append(question_module_map[question_number])

    return recommended_modules


def generate_feedback(recommended_modules):
    feedback = []
    with open(app.config.get('COURSE_MODULES_FILENAME'), encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for module_info in reader:
            if module_info.get('module_no') in recommended_modules:
                feedback.append((module_info.get('title'),
                                 module_info.get('url'),
                                 module_info.get('x-rel'),
                                 module_info.get('y-rel')))

    return feedback


if __name__ == '__main__':
    app.run(debug=False, port=5000)
