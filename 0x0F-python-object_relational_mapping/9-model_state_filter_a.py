#!/usr/bin/python3
"""
lists all State objects that contain the letter a from the db hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    accessign db and listing objects with a 
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(State.name.contains('a')):
        print('{0}: {1}'.format(instance.id, instance.name))
