from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'welcome to server 2 '
@app.route('/server2')
def index2():
    return 'welcome to server 2 '

if __name__ == '__main__':
    app.run( host='localhost',port=5002)
