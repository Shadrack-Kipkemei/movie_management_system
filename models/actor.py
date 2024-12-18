from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import Base
from models.movie_actors import movie_actors

# Actor model
class Actor(Base):
    __tablename__ = 'actors' # Table name in the database

    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String, nullable=False)   # Actor name

    # Relationship with movie through the association table movie_actors
    movies = relationship('Movie', secondary=movie_actors, back_populates='actors')

    # Class method to create new actor
    @classmethod
    def create(cls, session, name):
        actor = cls(name=name) # Create an instance of Actor with the given name
        session.add(actor) # Add the new actor to the session
        session.commit() # Commit the session to save the actor to the database
        return actor # return the created actor object

    # class method to retrieve all actors from the database
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all() # Query the Actor table and return all records

    # Class method to find an actor by their ID
    @classmethod
    def find_by_id(cls, session, actor_id):
        return session.query(cls).get(actor_id) # Query the Actor table to find the actor by ID

    # Class method to delete an actor by their ID
    @classmethod
    def delete(cls, session, actor_id):
        actor = cls.find_by_id(session, actor_id) # Find the actor by ID
        if actor:                                 # If actor exists
            session.delete(actor)                 # Delete the actor from the session
            session.commit()                      # Commit the session to save the changes
