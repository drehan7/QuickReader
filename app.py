from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from flask import Flask, render_template, url_for, request, flash, redirect

from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some secrety shit right here'
Bootstrap(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        req = request.form
        words = split_user_input(req)
        if len(words) > 0:
            return reader()
        else:
            flash("Enter text below")
            return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/reader')
def reader():
    words = request.form.get('user_input').split()
    i = 0
    word = words[i]
    return render_template('reader.html', word=word)


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
