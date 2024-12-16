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

    @classmethod
    def create(cls, session, name):
        actor = cls(name=name)
        session.add(actor)
        session.commit()
        return actor

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, actor_id):
        return session.query(cls).get(actor_id)

    @classmethod
    def delete(cls, session, actor_id):
        actor = cls.find_by_id(session, actor_id)
        if actor:
            session.delete(actor)
            session.commit()
