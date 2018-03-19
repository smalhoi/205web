from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Required
from wtforms.widgets import TextArea

from model import Session, Feedback, Character


session = Session()

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="2ocFLZpw1S95",
    WTF_CSRF_SECRET_KEY="2ocFLZpw1S95"
))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    info = session.query(Character).all()

    return render_template('search.html', info=info)


@app.route('/book')
def book():
    return render_template('book.html')


@app.route('/check')
def check():
    return render_template('check.html')


class fbForm(FlaskForm):

    name = StringField('name', validators=[Required()])
    phone = StringField('name', validators=[Required()])
    email = StringField('name', validators=[Required()])
    question = StringField('name', widget=TextArea(), validators=[Required()])


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = fbForm()
    if form.validate_on_submit():
        f = Feedback(name=form.name.data, phone=form.phone.data,
                     email=form.email.data, question=form.question.data)
        session.add(f)
        session.commit()
        return redirect(url_for('index'))
    return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
