#!/usr/bin/python3
"""
Defining the class City
"""


from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    Defining the class City

    Attributes:
        id(int): the id of city
        name(string): the city name
        state_id(int): foreign key to states.id

    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
