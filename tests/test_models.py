import unittest
from models.movie import Movie
from models.actor import Actor
from models.director import Director
from database.connection import SessionLocal


# Test class for models
class TestModels(unittest.TestCase):

    def setUp(self):
        self.session = SessionLocal()
        self.session.begin_nested()

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    # Test creating a movie
    def test_create_movie(self):
        director = Director(name = "Steven Spielberg")
        self.session.add(director)
        self.session.commit()

        movie = Movie(title = "Jaws", release_year = 1975, director_id = director.id)
        self.session.add(movie)
        self.session.commit()

        # retrieve and check movie
        retrieved_movie = self.session.query(Movie).filter_by(title = "Jaws")
        self.assertEqual(retrieved_movie.title, "Jaws")

if __name__ == '__main__':
    unittest.main()