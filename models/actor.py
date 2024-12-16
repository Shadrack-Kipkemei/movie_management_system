from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base
from models.movie_actors import movie_actors

# Actor model
class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String, nullable=False)   # Actor name

    # Relationship with movie (association table)
    movies = relationship('Movie', secondary=movie_actors, back_populates='actors')
