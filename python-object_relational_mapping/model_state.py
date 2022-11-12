#!/usr/bin/python3
""" Model model_state.py """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import delcarative_base

Base = delcarative_base()


class State(Base):
    """ Define a SQL model with SQLAlchemy """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True
                )
    name = Column(String(128), nullable=False)
