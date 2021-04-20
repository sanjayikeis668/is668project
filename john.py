from flask import Flask

app = Flask(__name__)

@app.route('/john')
def john():
    return "john"

if __name__ == '__main__':
    app.run()