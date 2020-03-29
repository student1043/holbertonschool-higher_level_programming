#!/usr/bin/python3
""" List cities """
if __name__ == "__main__":
    import sys
    from model_city import City
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    query = session.query(City, State).filter(City.state_id == State.id)
    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
