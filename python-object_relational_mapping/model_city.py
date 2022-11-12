#!/usr/bin/python3
'''
Model state from task 6
'''

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    '''
    Define a class called state
    that inherits from Base

    This class represent a SQL table
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True
                )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)
