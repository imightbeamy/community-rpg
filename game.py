import os
import flask
from flask import request, jsonify
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

# API routes

@app.route('/api/question/<int:question_id>', methods = ['GET'])
def get_question(question_id):
    return jsonify(api.get_question(question_id))

@app.route('/api/question', methods = ['POST'])
def post_question():
    text = request.form.get('text')
    return jsonify(api.add_question(text))

@app.route('/api/question/<int:question_id>', methods = ['PUT'])
def update_question(question_id):
    text = request.form.get('text')
    return jsonify(api.update_question(question_id, text))

@app.route('/api/question/<int:question_id>', methods = ['DELETE'])
def delete_question(question_id):
    return jsonify(api.delete_question(question_id))

@app.route('/api/token/<int:token_id>', methods = ['GET'])
def get_token(token_id):
    return jsonify(api.get_token(token_id))

@app.route('/api/token', methods = ['POST'])
def post_token():
    title = request.form.get('title')
    return jsonify(api.add_token(title))

@app.route('/api/token/<int:token_id>', methods = ['PUT'])
def update_token(token_id):
    title = request.form.get('title')
    return jsonify(api.update_token(token_id, title))

@app.route('/api/token/<int:token_id>', methods = ['DELETE'])
def delete_token(token_id):
    return jsonify(api.delete_token(token_id))
