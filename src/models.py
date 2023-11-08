import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base, backref
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



#This is for the blog users
class User(Base):
    __tablename__ = "Users"
    #Columns
    ID = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)

    #Relationships
    favorites = relationship("Favorites", backref="user") #establish a bidirectional relationship between User class and Favorite class



#Users can save their fav planets and characters, BRIDGE?
class Favorite(Base): #✔
    __tablename__ = "Favorites"
    #Columns
    ID = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('Users.ID')) #foreignkey to User 
    planet_id = Column(Integer, ForeignKey('Planets.ID')) #foreignkey to Planet 
    character_id = Column(Integer, ForeignKey('Characters.ID')) #foreignkey to Character 

    #Relationships
    user = relationship("Users", backref="favorites")  #Establish relationship with User table, remove '_id' suffix
    planet = relationship("Planets") #Relationship with Planet table, no established way to navigate back from Planet to Favorite.
    character = relationship("Characters") #Rel. with Character 




class Character(Base):
    __tablename__ = "Characters"
    # Columns
    ID = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    homeplanet_id = Column(Integer, ForeignKey('Planets.ID')) # foreign key to Planet
    starships_id = Column(Integer, ForeignKey('Starships.ID')) # foreign key to Starship
    birth_year = Column(String(250), nullable=False)

    # Relationships
    homeplanet = relationship('Planets', backref='residents') # 1 to many
    starships = relationship('Starship', backref='pilots') # 1 to many


class Planet(Base):
    __tablename__ = "Planets"
    #Columns
    ID = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    residents_id = Column(Integer, ForeignKey('Characters.ID')) #Foreignkey characters

    #Relationships
    residents = relationship("Characters", backref="homeplanet") #1 planet has many characters, characters have 1 planet



class Starship(Base):
    __tablename__ = "Starships"
    #Columns
    ID = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    starship_class = Column(String(250), nullable=False)
    pilots_id = Column(Integer, ForeignKey('Characters.ID')) #foreignkey characters

    #Relationships
    pilots = relationship("Characters", backref="starships")



class Specie(Base):
    __tablename__ = "Species"
    #Columns
    ID = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(250), nullable=False)
    classification = Column(String(250), nullable=False)
    homeplanet_id = Column(Integer, ForeignKey('Planets.ID')) #foreignkey planet
    people_id = Column(Integer, ForeignKey('Characters.ID')) #foreignkey characters

    #Relationships
    homeplanet = relationship("Planets", backref="species")
    people = relationship("Characters", backref="specie")



class Film(Base):
    __tablename__ = "Films"
    #Columns
    ID = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(250), nullable=False)
    episode_id  = Column(Integer, unique=True)
    director = Column(String(250), nullable=False)
    species_id = Column(Integer, ForeignKey('Species.ID')) #foreignkey specie

    #Relationships
    species = relationship("Species", backref="film")




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
