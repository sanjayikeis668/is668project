
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/john')
def john():
    return 'John'

@app.route('/paul')
def paul():
    return 'Paul'

@app.route('/george')
def george():
    return 'George'

@app.route('/pip')
def pip():
    return render_template('pip.html', name='PIP')

@app.route('/flask')
def flasks():
    return render_template('flasks.html', name = 'Flask')

@app.route('/template')
def template():
    return render_template('template.html', name = 'Template')

@app.route('/route')
def route():
    return render_template('route.html', name = 'route')

