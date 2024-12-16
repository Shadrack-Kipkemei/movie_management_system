import sys 
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import create_engine
from models.base import Base
from models.movie import Movie
from models.actor import Actor
from models.director import Director
from models.movie_actors import movie_actors


# create all tables in the database
def create_tables():
    engine = create_engine('sqlite:///movies.db')
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()