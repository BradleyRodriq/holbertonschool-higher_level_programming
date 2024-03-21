#!/usr/bin/python3
""" prints the first state object """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    """ get a state from the database """

    dtb = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(dtb)
    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = session.query(State).filter(State.id == '2').first()
    new_state.name = 'New Mexico'
    session.commit()
    session.close()
