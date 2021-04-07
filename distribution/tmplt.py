from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/distribution', methods=['GET', 'POST'])
def login():
    users = ["Mark Watts", "James Jameson", "Theodor Mitchell", "Steve Carson", "John Alt"]
    return render_template('distribution.html', title='Распределение по каютам', users=users)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
