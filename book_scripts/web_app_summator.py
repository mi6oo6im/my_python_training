from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        first_value = float(request.form.get('firstNumber'))
        second_value = float(request.form.get('secondNumber'))
        result = eval(str(first_value + second_value))
        return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run()
