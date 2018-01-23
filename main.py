from flask import Flask, render_template, url_for, redirect
from forms import MainQuestionnaire
import csv

app = Flask(__name__)
app.secret_key="\n\xd4\x0c\xec%\x12\xa1\xb95b\x89\xdaF'Ay\x1f\xc8"

@app.route('/')
def index():
    # return render_template('index.html')
    return redirect(url_for('assessment'))

@app.route('/assessment', methods=['GET', 'POST'])
def assessment():
    form = MainQuestionnaire()
    if form.validate_on_submit():
        answers = {}
        for field in form:
            # Process question fields (discarding submit and csrf)
            if field.id.startswith("q"):
                answers[field.id]=field.data
        recommended_modules = recommend_modules(answers)
        feedback = generate_feedback(recommended_modules)
        return render_template('feedback.html', feedback=feedback)

    return render_template('assessment.html', form=form)

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
    recommended_modules = []
    for question_number in answers:
        if not answers[question_number] == 'Ja':
            recommended_modules.append(question_module_map[question_number])

    return recommended_modules

def generate_feedback(recommended_modules):
    feedback=[]
    with open('course_modules.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for module_info in reader:
            if module_info.get('module_no') in recommended_modules:
                feedback.append((module_info.get('title'),
                                 module_info.get('url'),
                                 module_info.get('x-rel'),
                                 module_info.get('y-rel')))

    return feedback



@app.route('/feedback')
def feedback(answers):
    return str(answers)

if __name__ == '__main__':
    app.run(debug=True, port=5000)