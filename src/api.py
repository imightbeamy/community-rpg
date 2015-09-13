import logging
import db

from model.question import Question

session = db.Session()

def get_token(token_id):
    return {
        'token_id': token_id,
        'title': "Thing %d" % token_id,
        'yes_effect': 6,
        'no_effect': -5,
    }

def get_question(question_id):
    question = session.\
                query(Question).\
                filter(Question.question_id==question_id).one()
    return question.format()

def add_question(text):
    question = Question(text=text)
    session.add(question)
    session.commit()
    return question.format()

def update_question(question_id, text):
    question = session.\
                query(Question).\
                filter(Question.question_id==question_id).one()
    question.text = text
    session.commit()
    return question.format()

def delete_question(question_id):
    question = session.\
                query(Question).\
                filter(Question.question_id==question_id).one()
    session.delete(question)
    session.commit()
    return question.format()

def get_game():
    return {
        'questions': [ q.format() for q in session.query(Question).all() ],
        'all_tokens': map(get_token, [3,4,5,6,7])
    }