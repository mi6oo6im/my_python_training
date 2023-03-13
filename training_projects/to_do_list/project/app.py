from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '''	

    '''


@app.route('/result', methods=['POST'])
def result():
    pass
    return f'''	

    '''


if __name__ == '__main__':
    app.run()
