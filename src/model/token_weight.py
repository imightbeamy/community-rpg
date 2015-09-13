from sqlalchemy import Column, Integer, String
from src.db import Base

class TokenWeight(Base):
    __tablename__ = 'token_weights'

    question_id = Column(Integer, primary_key=True)
    token_id = Column(Integer)
    yes_weight = Column(Integer)
    no_weight = Column(Integer)

    def format(self):
        return {
            'question_id': self.question_id
            'token_id': self.token_id,
            'yes_weight': yes_weight,
            'no_weight': no_weight
        }

     __repr__(self):
       return "<TokenWeight %s>" % (self.format())