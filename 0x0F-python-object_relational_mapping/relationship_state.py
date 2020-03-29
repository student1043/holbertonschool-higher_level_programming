#!/usr/bin/python3
""" Model Class """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from model_state import Base


class City(Base):
        """ City Class """
        __tablename__ = 'cities'
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
root@5826afd85bc9:~/higher/0x0F-python-object_relational_mapping# emacs relationship_city.py
root@5826afd85bc9:~/higher/0x0F-python-object_relational_mapping# cat model_state.py
#!/usr/bin/python3
""" Model Class """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
        """ State Class """
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
