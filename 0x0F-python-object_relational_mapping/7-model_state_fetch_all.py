#!/usr/bin/python3
"""Script to list all `State` objects from the database `hbtn_0e_6_usa`."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

engine = create_engine('mysql+mysqldb://'
                       '{}:{}@localhost/{}'
                       .format(sys.argv[1],
                               sys.argv[2],
                               sys.argv[3]))
Session = sessionmaker(bind=engine)
session = Session()
for state in session.query(State).order_by(State.id):
    print("{}: {}".format(state.id, state.name))
