import flask
from flask import request
from count_appearance import count_appearance, CountAppearanceException

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "Посчитать присутсвие можно в службе <a href='http://127.0.0.1:5000/appearance'> appearance</a>"


help_msg = """<p>Укажите интервалы в параметрах 'lesson', 'pupil', 'tutor'</p>
                <p>Пример: <a href='http://127.0.0.1:5000/appearance?lesson=1&lesson=6&pupil=2&pupil=4&tutor=1&tutor=4'>
                http://127.0.0.1:5000/appearance?lesson=1&lesson=6&pupil=2&pupil=4&tutor=1&tutor=4</a></p>"""


@app.route('/appearance', methods=['GET'])
def appearance():
    data = {}
    try:
        data['lesson'] = [int(item) for item in request.args.getlist('lesson')]
        data['pupil'] = [int(item) for item in request.args.getlist('pupil')]
        data['tutor'] = [int(item) for item in request.args.getlist('tutor')]
    except KeyError:
        return help_msg
    except ValueError:
        return "Для указания интервалов используйте целые числа"
    else:
        if not (len(data['lesson']) and len(data['pupil']) and len(data['tutor'])):
            return help_msg
        try:
            ans = str(count_appearance(data))
        except CountAppearanceException as err:
            ans = str(err)
        return ans


app.run()
