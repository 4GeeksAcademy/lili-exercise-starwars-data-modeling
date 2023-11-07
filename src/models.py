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
    ID = Column()
    username = Column()
    password = Column()
    email = Column()

    #Relationships

#Users can save their fav planets and characters, BRIDGE?
class Favorite(Base):
    __tablename__ = "Favorite"
    #Columns
    ID = Column()
    user_id = Column() #foreignkey user
    planet_id = Column() #foreignkey planet
    character_id = Column() #foreignkey character

    #Relationships

class Character(Base):
    __tablename__ = "Character"
    #Columns
    ID = Column()
    name = Column()
    homeplanet_id = Column() #foreignkey planet
    starships_id = Column() #foreignkey starship
    birth_year = Column()

    #Relationships
    
class Planet(Base):
    __tablename__ = "Planet"
    #Columns
    ID = Column()
    name = Column()
    climate = Column()
    terrain = Column()
    residents_id = Column() #Foreignkey characters

    #Relationships

class Starship(Base):
    __tablename__ = "Starship"
    #Columns
    ID = Column()
    name = Column()
    starship_class = Column()
    pilots_id = Column() #foreignkey characters

    #Relationships

class Specie(Base):
    __tablename__ = "Specie"
    #Columns
    ID = Column()
    name = Column()
    classification = Column()
    homeplanet_id = Column() #foreignkey planet
    people_id = Column() #foreignkey characters

    #Relationships

class Films(Base):
    __tablename__ = "Films"
    #Columns
    ID = Column()
    title = Column()
    episode_id  = Column()
    director = Column()
    characters_id = Column() #foreignkey characters
    species_id = Column() #foreignkey specie

    #Relationships



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
