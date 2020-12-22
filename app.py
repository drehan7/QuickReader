from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask import Flask, render_template, url_for, request, flash, redirect

from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some secrety stuff right here'
Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


user_words = list()


@app.route('/', methods=['GET', 'POST'])
def index():
    global user_words

    if request.method == "POST":
        req = request.form
        words = split_user_input(req)
        if len(words) > 0:
            user_words = words
            return redirect(url_for('reader'))
        else:
            flash("Enter text below")
            return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/reader', methods=['GET', 'POST'])
def reader():
    global user_words
    url = 'reader.html'
    i = 0
    if request.method == 'GET':
        return render_template(url, word=user_words[i])
    if request.method == 'POST' and request.form["one_button"] == "Next Word":
        i += 1
        print("Next button pressed")
    if request.method == 'POST' and request.form["one_button"] == "Previous Word":
        i = 0
        print("Prev button pressed")
        # elif request.form["prev_button"] == "Previous Word":
        #     if i > 0:
        #         i -= 1

    print(len(user_words))
    print("i = ", i)
    return render_template(url, word=user_words[i])


def word_nav():
    pass


def split_user_input(user_input):
    words = list()
    userStr = user_input.get('user_input')
    splitUserStr = userStr.split()
    for i in splitUserStr:
        words.append(i)
    return words


if __name__ == "__main__":
    app.run(debug=True)
