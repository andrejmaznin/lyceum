from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<title>')
def page(title):
    return render_template('base.html', title=title)


@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def professions(prof):
    return render_template('base.html', prof=prof, img1=url_for('static', filename='img/train.png'),
                           img2=url_for('static', filename='img/sims.png'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
