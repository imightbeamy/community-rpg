import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is a game!'

@app.route('/manage')
def manage():
    return 'Manage RPG!'