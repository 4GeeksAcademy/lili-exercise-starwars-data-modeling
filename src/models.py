import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#This is for the blog users
class User(Base):
    __tablename__ = "User"
    #Columns

    #Relationships

#Users can save their fav planets and characters
class Favorite(Base):
    __tablename__ = "Favorite"
    #Columns

    #Relationships

class Character(Base):
    __tablename__ = "Name"
    #Columns

    #Relationships
    
class Planet(Base):
    __tablename__ = "Planet"
    #Columns

    #Relationships

class Starship(Base):
    __tablename__ = "Starship"
    #Columns

    #Relationships

class Specie(Base):
    __tablename__ = "Specie"
    #Columns

    #Relationships

class Films(Base):
    __tablename__ = "Films"
    #Columns

    #Relationships



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
