from flask import Flask, render_template, url_for, redirect
from forms import MainQuestionnaire

app = Flask(__name__)
app.secret_key='verysecrethere'

@app.route('/')
def index():
    return redirect(url_for('assessment'))

@app.route('/assessment', methods=['GET', 'POST'])
def assessment():
    form = MainQuestionnaire()
    if form.validate_on_submit():
        print("Form submitted and validated")
    return render_template('assessment.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5000)