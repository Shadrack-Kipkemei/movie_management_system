from database.connection import SessionLocal
from models.movie import Movie
from models.actor import Actor
from models.director import Director

def create_director(session, director_name):
    director = session.query(Director).filter_by(name=director_name).first()
    if not director:
        director = Director(name=director_name)
        session.add(director)
        session.commit()
    return director

def create_movie(session, title, release_year, director_id):
    movie = Movie(title=title, release_year=release_year, director_id=director_id)
    session.add(movie)
    session.commit()
    return movie

def create_actor(session, actor_name):
    actor = session.query(Actor).filter_by(name=actor_name).first()
    if not actor:
        actor = Actor(name=actor_name)
        session.add(actor)
        session.commit()
    return actor

def add_movie():
    title = input("Enter the movie title: ")
    release_year = input("Enter the release year: ")
    director_name = input("Enter the director's name: ")

    try:
        release_year = int(release_year)
    except ValueError:
        print("Invalid input for release year. Please enter a valid integer.")
        return

    session = SessionLocal()
    director = create_director(session, director_name)
    movie = create_movie(session, title, release_year, director.id)
    print(f"Added movie: {title} (Director: {director_name})")

def add_actor():
    movie_title = input("Enter the movie title: ")
    actor_name = input("Enter the actor's name: ")

    session = SessionLocal()
    movie = session.query(Movie).filter_by(title=movie_title).first()
    if not movie:
        print(f"Movie '{movie_title}' not found.")
        return

    actor = create_actor(session, actor_name)
    movie.actors.append(actor)
    session.commit()
    print(f"Added actor: {actor_name} to movie: {movie_title}")

def list_all_movies():
    session = SessionLocal()
    movies = session.query(Movie).all()
    for movie in movies:
        print(f"{movie.id}. {movie.title} ({movie.release_year})")

def list_all_actors():
    session = SessionLocal()
    actors = session.query(Actor).all()
    for actor in actors:
        print(f"{actor.id}. {actor.name}")

def delete_movie():
    movie_id = input("Enter the movie ID to delete: ")
    try:
        movie_id = int(movie_id)
    except ValueError:
        print("Invalid input. Please enter a valid movie ID.")
        return
    session = SessionLocal()
    movie = session.query(Movie).filter_by(id=movie_id).first()
    if movie:
        session.delete(movie)
        session.commit()
        print(f"Deleted movie with ID {movie_id}")
    else:
        print(f"Movie with ID {movie_id} not found.")

def delete_actor():
    actor_id = input("Enter the actor ID to delete: ")
    try:
        actor_id = int(actor_id)
    except ValueError:
        print("Invalid input. Please enter a valid actor ID.")
        return
    session = SessionLocal()
    actor = session.query(Actor).filter_by(id=actor_id).first()
    if actor:
        session.delete(actor)
        session.commit()
        print(f"Deleted actor with ID {actor_id}")
    else:
        print(f"Actor with ID {actor_id} not found.")

def main():
    while True:
        print("\n1. Add Movie")
        print("2. Add Actor to Movie")
        print("3. List All Movies")
        print("4. List All Actors")
        print("5. Delete Movie")
        print("6. Delete Actor")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_movie()
        elif choice == '2':
            add_actor()
        elif choice == '3':
            list_all_movies()
        elif choice == '4':
            list_all_actors()
        elif choice == '5':
            delete_movie()
        elif choice == '6':
            delete_actor()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please enter 1-7.")

if __name__ == "__main__":
    main()