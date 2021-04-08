from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
import os
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

app = Flask(__name__)


@app.route('/gallery', methods=['POST', 'GET'])
def galery():
    title = "Пейзажи Марса"
    pictures = os.listdir('static/img')
    if request.method == 'GET':
        return render_template('load.html', pictures=pictures, title=title, lnp=len(pictures))
    elif request.method == 'POST':
        f = request.files['file']
        with open(f'static/img/{len(pictures) + 1}.jpg', 'wb') as file:
            file.write(f.read())
        return redirect('/gallery')


@app.route('/member')
def member():
    with open(f'templates/members.json', mode='rb', ) as file:
        data = json.load(file)
    for i in range(len(data)):
        data[i]["professions"] = list(sorted(data[i]["professions"]))

    return render_template("member.html", data=data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
