from database.connection import SessionLocal
from models.movie import Movie
from models.actor import Actor
from models.director import Director

def add_movie():
    # Prompt the user for input
    title = input("Enter the movie title: ")
    release_year = input("Enter the release year: ")
    director_name = input("Enter the director's name: ")

    session = SessionLocal()
    # Find or create director
    director = session.query(Director).filter_by(name=director_name).first()
    if not director:
        director = Director(name=director_name)
        session.add(director)
        session.commit()

    # Create and add movie
    new_movie = Movie(title=title, release_year=int(release_year), director_id=director.id)
    session.add(new_movie)
    session.commit()
    print(f"Added movie: {title} (Director: {director_name})")

def add_actor():
    # Prompt the user for input
    title = input("Enter the movie title: ")
    actor_name = input("Enter the actor's name: ")

    session = SessionLocal()
    # Find movie and actor
    movie = session.query(Movie).filter_by(title=title).first()
    actor = session.query(Actor).filter_by(name=actor_name).first()
    if not actor:
        actor = Actor(name=actor_name)
        session.add(actor)
        session.commit()

    # Add actor to movie
    movie.actors.append(actor)
    session.commit()
    print(f"Added actor: {actor_name} to movie: {title}")

def main():
    while True:
        print("1. Add Movie")
        print("2. Add Actor to Movie")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_movie()
        elif choice == '2':
            add_actor()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
