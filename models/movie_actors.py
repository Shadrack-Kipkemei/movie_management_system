from sqlalchemy import Table, Column, Integer, ForeignKey
from models.base import Base

# Association table between movies and actors
movie_actors = Table(
    'movie_actors', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)
