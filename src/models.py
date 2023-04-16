import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey ('user.id'))
    basic_data_id = Column(Integer)

    basic_data = relationship("Basic_data", back_populates="favorites")

class Basic_data(Base):
    __tablename__ = 'basic_data'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    favorites = relationship("Favorites", back_populates="basic_data")
    character = relationship("Character", uselist=False, back_populates="basic_data")
    planet = relationship("Planet", uselist=False, back_populates="basic_data")
    

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    gender = Column(String)
    hair_color = Column(String)
    eye_color = Column(String)
    basic_data_id = Column(Integer, ForeignKey('basic_data.id'))

    basic_data = relationship("Basic_data", back_populates="character")


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    population = Column(Integer)
    terrain = Column(String)
    climate = Column(String)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)
    basic_data_id = Column(Integer, ForeignKey('basic_data.id'))

    basic_data = relationship("Basic_data", back_populates="planet")




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
