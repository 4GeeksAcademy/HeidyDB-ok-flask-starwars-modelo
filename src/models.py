from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import String, Boolean, Integer,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


db = SQLAlchemy()


class User(db.Model):
    __tablename__= 'user' # se le pone el mismo nombre de la clase en minuscula
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    favorites: Mapped[list['FavoriteCharacteres']]= relationship(back_populates ='user' )


class Characters(db.Model):
    __tablename__ = 'characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(50), nullable=False, unique= True)
    heigth: Mapped[int] = mapped_column(Integer)
    weigth: Mapped[int] = mapped_column(Integer)
    favorite_by: Mapped[list['FavoriteCharacteres']]= relationship(
        back_populates= 'characters', cascade='all, delete-orphan') #este 'user' viene de la tabla FavoriteCharacters , las enlaza  


class FavoriteCharacteres(db.Model):
    __tablename__= 'favorite_characters'
    id: Mapped[int] = mapped_column(Integer, primary_key= True)
    user_id: Mapped[int]= mapped_column(ForeignKey('user.id'))
    user : Mapped[User] = relationship(back_populates= 'favorites')
    character_id: Mapped[int] = mapped_column(ForeignKey('characters.id'))
    characters: Mapped[Characters] = relationship(
        back_populates = 'favorite_by', cascade='all, delete-orphan')
   
class Planets(db.Model):
    __tablename__= 'planets'
    id: Mapped[int]= mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    population: Mapped[int]= mapped_column(Integer)
    diameter: Mapped[int] = mapped_column(Integer)
    favorite_by: Mapped[list['FavoritePlanets']]= relationship(
        back_populates= 'favorite_by', cascade='all, delete-orphan')


class FavoritePlanets(db.Model):
    __tablename__='favorite_planets'
    id: Mapped[int] = mapped_column(Integer, primary_key= True)
    user_id: Mapped[int]= mapped_column(ForeignKey('user.id'))
    user : Mapped[User] = relationship(back_populates= 'favorites')
    planet_id: Mapped[int] = mapped_column(ForeignKey('planets.id'))
    planets: Mapped[Characters] = relationship(
        back_populates = 'favorite_by', cascade='all, delete-orphan')
