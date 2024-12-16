from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base


#Actor model
class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key = True) # Primary key
    name = Column(String, nullable = False) # Actor name

    # Relationship with movie
    movies = relationship('Movie', secondary = 'movie-actors', back_populates = 'actors')