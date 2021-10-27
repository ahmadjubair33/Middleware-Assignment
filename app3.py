
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'welcome to server 3 '
@app.route('/server3')
def index3():
    return 'welcome to server 3 '


if __name__ == '__main__':
    app.run( host='localhost',port=5003)
