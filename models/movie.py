from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.movie_actors import movie_actors


# Movie model
class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True) # Primary key
    title = Column(String, nullable=False) # Movie title
    release_year = Column(Integer) # Release year
    director_id = Column(Integer, ForeignKey('directors.id')) # Foreign key to director

    # Relationships
    director = relationship('Director', back_populates = 'movies')
    actors = relationship('Actor', secondary = 'movie_actors', back_populates = 'movies')