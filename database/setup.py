from sqlalchemy import create_engine
from models.base import Base
from models.movie import Movie
from models.actor import Actor
from models.director import Director


# create all tables in the database
def create_tables():
    engine = create_engine('sqlite3:///movies.db')
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_tables()