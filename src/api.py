import db
from model.question import Question
from model.token import Token

session = db.Session()

# Quesetions
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

# Tokens
def get_token(token_id):
    token = session.\
                query(Token).\
                filter(Token.token_id==token_id).one()
    return token.format()

def add_token(title):
    token = Token(title=title)
    session.add(token)
    session.commit()
    return token.format()

def update_token(token_id, title):
    token = session.\
                query(Token).\
                filter(Token.token_id==token_id).one()
    token.title = title
    session.commit()
    return token.format()

def delete_token(token_id):
    token = session.\
                query(Token).\
                filter(Token.token_id==token_id).one()
    session.delete(token)
    session.commit()
    return token.format()

def get_game():
    return {
        'questions': [ q.format() for q in session.query(Question).all() ],
        'all_tokens': [ t.format() for t in session.query(Token).all() ],
    }