from sqlalchemy import Column, Integer, String
from src.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from src.model.token import Token

class TokenWeight(Base):
    __tablename__ = 'token_weights'

    question_id = Column(Integer, ForeignKey('questions.question_id'), primary_key=True)
    token_id = Column(Integer, ForeignKey('tokens.token_id'), primary_key=True)
    yes_weight = Column(Integer)
    no_weight = Column(Integer)

    token = relationship("Token")

    def format(self):
        return {
            'question_id': self.question_id,
            'token_id': self.token_id,
            'title': self.token.title if self.token != None else "No title",
            'yes_weight': self.yes_weight,
            'no_weight': self.no_weight
        }

    def __repr__(self):
       return "<TokenWeight %s>" % (self.format())