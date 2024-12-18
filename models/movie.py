from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.movie_actors import movie_actors

# Movie model
class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)  # Primary key
    title = Column(String, nullable=False)  # Movie title
    release_year = Column(Integer)          # Release year
    director_id = Column(Integer, ForeignKey('directors.id'))  # Foreign key to director

    # Relationships
    director = relationship('Director', back_populates='movies')
    actors = relationship('Actor', secondary=movie_actors, back_populates='movies')

    @classmethod
    def create(cls, session, title, release_year, director_id):
        movie = cls(title=title, release_year=release_year, director_id=director_id)
        session.add(movie)
        session.commit()
        return movie

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, movie_id):
        return session.query(cls).get(movie_id)

    @classmethod
    def delete(cls, session, movie_id):
        movie = cls.find_by_id(session, movie_id)
        if movie:
            session.delete(movie)
            session.commit()
