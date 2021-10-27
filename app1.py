from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'welcome to server 1 '
@app.route('/server1')
def index1():
    return 'welcome to server 1 '

if __name__ == '__main__':
    app.run( host='localhost',port=5001) 
