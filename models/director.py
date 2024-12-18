from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base

# Director model
class Director(Base):
    __tablename__ = 'directors'

    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String, nullable=False)   # Director name

    # Relationship with movie
    movies = relationship('Movie', back_populates='director')

    # Class method to create a new director
    @classmethod
    def create(cls, session, name):
        director = cls(name=name) # Create a new instance of the director class with the given name
        session.add(director) # Add the new director instance to the session
        session.commit() # Commit the session to the save the new director to the database
        return director # Return the created instance

    # Class method to retrieve all the directors from the database
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all() # Query the director table and return a list of all the director record

    # Class method to find a director by their ID
    @classmethod
    def find_by_id(cls, session, director_id):
        return session.query(cls).get(director_id) # Query the director table and return the director with the given ID

    # Class method to delete a director by their ID
    @classmethod
    def delete(cls, session, director_id):
        director = cls.find_by_id(session, director_id) # Find the director by their ID
        if director: # Check if the director exists from the session
            session.delete(director) # Delete the director from the session
            session.commit() # Commit the session to save changes
