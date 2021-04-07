from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<title>')
def page(title):
    return render_template('base.html', title=title)


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    data = {"title": "Анкета", "surname": "Jackson", "name": "Jeremy", "education": "Высшее",
            "profession": "Оператор БПЛА", "sex": "male", "motivation": "Интересуюсь космической тематикой",
            "ready": "true"}
    return render_template('auto_answer.html', **data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
