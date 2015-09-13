from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.model.token_weight import TokenWeight
from src.db import Base

class Question(Base):
    __tablename__ = 'questions'

    question_id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    order = Column(Integer)

    token_weights = relationship("TokenWeight")

    def format(self):
        return {
            'question_id': self.question_id,
            'text': self.text,
            'tokens': [ tw.format() for tw in self.token_weights ],
            'unset_tokens': None,
            'has_unset_tokens': False
        }

    def __repr__(self):
       return "<Question %s>" % (self.format())