#!/usr/bin/python3
''' State model '''

from sqlalchemy.ext.declarative import delcarative_base
from sqlalchemy import Column, Integer, String

Base = delcarative_base()


class State(Base):
    '''
        SQL Model State with SQLAlchemy
    '''

    __tablename__ = "states"

    id = Column(Integer(), primary_key=True,
                nullable=False, unique=True,
                autoincrement=True
                )
    name = Column(String(128), nullable=False)
