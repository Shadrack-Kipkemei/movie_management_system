from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base


# Director model
class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key = True) # Primary key
    name = Column(String, nullable = False) # Directors name

    # Relationship with movie
    movies = relationship('Movie', back_populates = 'director')