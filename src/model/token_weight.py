from sqlalchemy import Column, Integer, String
from src.db import Base

class TokenWeight(Base):
    __tablename__ = 'token_weights'

    question_id = Column(Integer, primary_key=True)
    token_id = Column(Integer)
    yes_weight = Column(Integer)
    no_weight = Column(Integer)

    def __repr__(self):
       return "<Token (token_id='%s', title='%s')>" % (self.token_id, self.title)