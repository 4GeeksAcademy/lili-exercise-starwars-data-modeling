import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base, backref
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



#This is for the blog users
class User(Base):
    __tablename__ = "User"
    #Columns
    ID = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)

    #Relationships
    favorites = relationship("Favorite", backref="user") #establish a bidirectional relationship between User class and Favorite class



#Users can save their fav planets and characters, BRIDGE?
class Favorite(Base): #✔
    __tablename__ = "Favorite"
    #Columns
    ID = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('User.ID')) #foreignkey to User 
    planet_id = Column(Integer, ForeignKey('Planet.ID')) #foreignkey to Planet 
    character_id = Column(Integer, ForeignKey('Character.ID')) #foreignkey to Character 

    #Relationships
    user = relationship("User", backref="favorites")  #Establish relationship with User table, remove '_id' suffix
    planet = relationship("Planet") #Relationship with Planet table, no established way to navigate back from Planet to Favorite.
    character = relationship("Character") #Rel. with Character 




class Character(Base):
    __tablename__ = "Character"
    #Columns
    ID = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    homeplanet_id = Column(Integer, ForeignKey('Planet.ID')) #foreignkey planet
    starships_id = Column(Integer, ForeignKey('Starship.ID')) #foreignkey starship
    birth_year = Column(String(250), nullable=False)

    #Relationships
    homeplanet = relationship('Planet') #1 to 1
    starships = relationship('Starship') #1 to many


class Planet(Base):
    __tablename__ = "Planet"
    #Columns
    ID = Column(Integer, primary_key=True, nullable=False)
    name = Column()
    climate = Column()
    terrain = Column()
    residents_id = Column(Integer, ForeignKey('Character.ID')) #Foreignkey characters

    #Relationships
    residents = relationship("Character", backref="homeplanet") #1 planet has many characters, characters have 1 planet



class Starship(Base):
    __tablename__ = "Starship"
    #Columns
    ID = Column(Integer, primary_key=True, nullable=False)
    name = Column()
    starship_class = Column()
    pilots_id = Column() #foreignkey characters

    #Relationships




class Specie(Base):
    __tablename__ = "Specie"
    #Columns
    ID = Column(Integer, primary_key=True, nullable=False)
    name = Column()
    classification = Column()
    homeplanet_id = Column() #foreignkey planet
    people_id = Column() #foreignkey characters

    #Relationships




class Films(Base):
    __tablename__ = "Films"
    #Columns
    ID = Column(Integer, primary_key=True, nullable=False)
    title = Column()
    episode_id  = Column()
    director = Column()
    characters_id = Column() #foreignkey characters
    species_id = Column() #foreignkey specie

    #Relationships





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
