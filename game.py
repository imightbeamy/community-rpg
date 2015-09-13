import os
import flask
import sys
import logging
import pystache
from src import api

app = flask.Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

def mustache_render(tpl_file, data):
    return pystache.render(open('templates/' + tpl_file, 'r').read(), data)

@app.route('/')
def index():
    return 'This is a game!'

@app.route('/manage')
def manage():
    return mustache_render('manage.mustache', api.get_game())
