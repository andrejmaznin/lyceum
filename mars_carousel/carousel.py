from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        file = url_for('static', filename='img/photo.jpg')

        return f'''<!doctype html>
                <html lang="en">
                <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style.css')}"/>
                    <title>Отбор астронавтов</title>
                </head>
                <body>
                <h1 align="center">Загрузка фотографии</h1>
                <h3 align="center">для участия в миссии</h3>
                <div>
                    <form class="login_form" method="post" enctype="multipart/form-data">
                        <div class="form-group">
                            <label for="photo">Приложите фотографию</label>
                            <input type="file" class="form-control-file" id="photo" name="file">
                        </div>
                        <img src="{file}" alt="Фото">
                        <br>
                        <button type="submit" class="btn btn-primary">Отправить</button>
                    </form>
                </div>
                </body>
                </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        with open(f'static/img/{f.filename}', 'wb') as file:
            file.write(f.read())
        file = url_for('static', filename=f'img/{f.filename}')
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Загрузка фотографии</h1>
                            <h3 align="center">для участия в миссии</h3>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                   <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <img src="{file}" alt="Фото">
                                    <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''


@app.route('/carousel', methods=['GET'])
def carousel():
    if request.method == 'GET':
        return f'''<!doctype html>
                    <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
                              integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                        <title>Отбор астронавтов</title>
                    
                    </head>
                    <body>
                    <h1 align="center">Пейзажи Марса</h1>
                    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
                    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                        <ol class="carousel-indicators">
                            <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                            <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                            <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                        </ol>
                        <div class="carousel-inner">
                            <div class="carousel-item active">
                                <img class="center" src="static/img/1.jpg">
                            </div>
                            <div class="carousel-item">
                                <img class="center" src="static/img/2.jpg">
                            </div>
                            <div class="carousel-item">
                                <img class="center" src="static/img/3.jpg">
                            </div>
                        </div>
                        <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                            <span class="carousel-control-prev-icon" aria-hidden="true" ></span>
                            <span class="sr-only">Previous</span>
                        </a>
                        <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                            <span class="carousel-control-next-icon" aria-hidden="true"></span>
                            <span class="sr-only">Next</span>
                        </a>
                    </div>
                    
                    </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
