from flask import Flask, request, jsonify, make_response
import json

app = Flask(__name__)

@app.route('/')
def index():
    return ("""
        <h2>Form here</h2>
        <form action="/set-cookie" method="POST">
            <input type="text" name="field"><br/>
            <input type="submit">
    """)


@app.route('/set-cookie', methods=['POST'])
def set_cookie():
    if request.method == 'POST':
        value = request.form.get('field')
        cookie_value = json.dumps(dict(field_name='field',
                                       value=value))
        resp = make_response("<p>Cookie set to {}</p>".format(cookie_value))
        seconds_valid = 60 * 60 * 24 * 365 * 5      # Five years in seconds
        resp.set_cookie('my_cookie', cookie_value, max_age=seconds_valid)
        return resp


@app.route('/get-cookie')
def get_cookie():
    cookie_value = request.cookies.get('my_cookie')
    return ("""
        <h2>Cookie value</h2>
        <p>Cooke value is {}</p>
    """.format(cookie_value))


if __name__ == '__main__':
    app.run()