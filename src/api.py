import db
from model.question import Question
from model.token import Token
from src.model.token_weight import TokenWeight

# Quesetions
def get_question(question_id):
    session = db.Session()
    question = session.\
                query(Question).\
                filter(Question.question_id==question_id).one()
    return question.format()

def add_question(text):
    session = db.Session()
    question = Question(text=text)
    session.add(question)
    session.commit()
    return question.format()

def update_question(question_id, text):
    session = db.Session()
    question = session.\
                query(Question).\
                filter(Question.question_id==question_id).one()
    question.text = text
    session.commit()
    return question.format()

def delete_question(question_id):
    session = db.Session()
    question = session.\
                query(Question).\
                filter(Question.question_id==question_id).one()
    session.delete(question)
    session.commit()
    return question.format()

# TokenWeights
def get_token_weight(question_id, token_id):
    session = db.Session()
    token_weight = session. \
                query(TokenWeight). \
                filter(TokenWeight.question_id==question_id). \
                filter(TokenWeight.token_id==token_id).one()
    return token_weight.format()

def add_token_weight(question_id, token_id, yes_weight, no_weight):
    session = db.Session()
    token_weight = TokenWeight(
                        question_id=question_id, \
                        token_id=token_id, \
                        yes_weight=yes_weight, \
                        no_weight=no_weight)
    session.add(token_weight)
    session.commit()
    return token_weight.format()

def update_token_weight(question_id, token_id, yes_weight, no_weight):
    session = db.Session()
    token_weight = session.\
                query(TokenWeight).\
                filter(TokenWeight.question_id==question_id). \
                filter(TokenWeight.token_id==token_id).one()
    token_weight.yes_weight = yes_weight
    token_weight.no_weight = no_weight
    session.commit()
    return token_weight.format()

def delete_token_weight(question_id, token_id):
    session = db.Session()
    token_weight = session.\
                query(TokenWeight).\
                filter(TokenWeight.question_id==question_id). \
                filter(TokenWeight.token_id==token_id).one()
    session.delete(token_weight)
    session.commit()
    return token_weight.format()

# Tokens
def get_token(token_id):
    session = db.Session()
    token = session.\
                query(Token).\
                filter(Token.token_id==token_id).one()
    return token.format()

def add_token(title):
    session = db.Session()
    token = Token(title=title)
    session.add(token)
    session.commit()
    return token.format()

def update_token(token_id, title):
    session = db.Session()
    token = session.\
                query(Token).\
                filter(Token.token_id==token_id).one()
    token.title = title
    session.commit()
    return token.format()

def delete_token(token_id):
    session = db.Session()
    token = session.\
                query(Token).\
                filter(Token.token_id==token_id).one()
    session.delete(token)
    session.commit()
    return token.format()

def get_game():
    session = db.Session()
    return {
        'questions': [ q.format() for q in session.query(Question).all() ],
        'all_tokens': [ t.format() for t in session.query(Token).all() ],
    }