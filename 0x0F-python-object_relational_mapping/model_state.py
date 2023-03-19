#!/usr/bin/python3
"""
contains class definition of state
making use of SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    This class links to the MySQL table

    Attributes:
        name(string): name of state
        id(int): identifier of state

    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
