from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.movie_actors import movie_actors

# Movie model
class Movie(Base):
    __tablename__ = 'movies'

    # Define the columns in the table
    id = Column(Integer, primary_key=True)  # Primary key
    title = Column(String, nullable=False)  # Movie title
    release_year = Column(Integer)          # Release year
    director_id = Column(Integer, ForeignKey('directors.id'))  # Foreign key to director

    # Relationships
    director = relationship('Director', back_populates='movies') # One to many relationship
    actors = relationship('Actor', secondary=movie_actors, back_populates='movies') # Many to many relationship

    # Class method to create new movie
    @classmethod
    def create(cls, session, title, release_year, director_id):
        movie = cls(title=title, release_year=release_year, director_id=director_id) # Create a new movie instance with provided details
        session.add(movie) # Add a movie to the session
        session.commit() # Commit the session to save the movie to the database
        return movie # return the newly created movie instance

    # Class method to retrieve all movies from the database
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    # Class method to find a movie by its ID
    @classmethod
    def find_by_id(cls, session, movie_id):
        return session.query(cls).get(movie_id)

    # class method to delete a movie by its ID
    @classmethod
    def delete(cls, session, movie_id):
        movie = cls.find_by_id(session, movie_id)
        if movie:
            session.delete(movie)
            session.commit()
