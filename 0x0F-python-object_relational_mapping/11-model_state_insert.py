#!/usr/bin/python3
"""
adds the State object "louisiana" to the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    accessing db and inserting data
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    add_state = State(name="Louisiana")
    session.add(add_state)
    session.commit()
    print(add_state.id)
    session.close()
