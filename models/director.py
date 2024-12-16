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

    @classmethod
    def create(cls, session, name):
        director = cls(name=name)
        session.add(director)
        session.commit()
        return director

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, director_id):
        return session.query(cls).get(director_id)

    @classmethod
    def delete(cls, session, director_id):
        director = cls.find_by_id(session, director_id)
        if director:
            session.delete(director)
            session.commit()
