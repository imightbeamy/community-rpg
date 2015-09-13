from sqlalchemy import Column, Integer, String
from src.db import Base

class Token(Base):
    __tablename__ = 'tokens'

    token_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)

    def format(self):
        return {
           'token_id': self.token_id,
           'title': self.title
        }

    def __repr__(self):
       return "<Token %s>" % (self.format())