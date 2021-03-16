from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index_of_index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promoution():
    return """Человечество вырастает из детства.
                </br>Человечеству мала одна планета.
               </br>Мы сделаем обитаемыми безжизненные пока планеты.
               </br>И начнем с Марса!  
                </br>Присоединяйся!"""


@app.route("/image_mars")
def image_mars():
    return f"""
                <h1>Жди нас, марс!</h1>
                <img src="{url_for("static", filename='img/mars.png')}">
                <p>Вот она какая, красная планета</p>
                """


@app.route("/promotion_image")
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                   <h1 class="text-danger">Жди нас, марс!</h1>
                    <img src="{url_for("static", filename='img/mars.png')}">
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!  
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!  
                    </div>
                  </body>
                </html>
                """


@app.route('/choice/<planet_name>')
def choice(planet_name):
    choice_list = [
        'Эта планета близка к Земле;',
        'На ней много необходимых ресурсов;',
        'На ней есть вода и атмосфера;',
        'На ней есть небольшое магнитное поле;',
        'Наконец, она просто красива!'
    ]
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {}</h1>
                    <h3>{}</h3>
                    <div class="alert-success" role="alert">
                      <br><h3>{}</h3>
                    </div>
                    <div class="alert-secondary" role="alert">
                      <br><h3>{}</h3>
                    </div>
                    <div class="alert-warning" role="alert">
                      <br><h3>{}</h3>
                    </div>
                    <div class="alert-danger" role="alert">
                      <br><h3>{}</h3>
                    </div>
                  </body>
                </html>""".format(planet_name, *choice_list)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {}:</h2>
                    <div class="alert-success" role="alert">
                      <br><h3>Поздравляем! Ваш рейтинг после {} этапа отбора</h3>
                    </div>
                    <br><h3>составляет {}!</h3>
                    <div class="alert-warning" role="alert">
                       <br><h2>Желаем удачи!</h2>
                    </div>
                  </body>
                </html>""".format(nickname, level, rating)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
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
                            <h1 align="center">Анкета претендента</h1>
                            <h3 align="center">на участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" aria-describedby="surnamelHelp" placeholder="Введите фамилию" name="surname">

                                    <input type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Введите имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="eduSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="edu">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Выше среднего</option>
                                          <option>Супер!</option>
                                        </select>
                                     </div>
                                        <label for="eduSelect">Какие у Вас есть профессии?</label>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="prof" name="prof">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof1">
                                        <label class="form-check-label" for="acceptRules">Инженер-строитель</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof2">
                                        <label class="form-check-label" for="acceptRules">Пилот</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof3">
                                        <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof4">
                                        <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof5">
                                        <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof6">
                                        <label class="form-check-label" for="acceptRules">Врач</label>
                                        <br><input type="checkbox" class="form-check-input" id="prof" name="prof7">
                                        <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                    </div>

                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['edu'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        print(request.form['prof'])
        print(request.form['prof1'])
        print(request.form['prof2'])
        print(request.form['prof3'])
        print(request.form['prof4'])
        print(request.form['prof5'])
        print(request.form['prof6'])
        print(request.form['prof7'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
