from database.connection import SessionLocal
from models.movie import Movie
from models.actor import Actor
from models.director import Director

# Function to create a director if the don't exist in the database
def create_director(session, director_name):
    # Query the director table to check if the director already exists by name
    director = session.query(Director).filter_by(name=director_name).first()
    # If the director is not found, create a new one
    if not director:
        director = Director(name=director_name)
        session.add(director)
        session.commit()
    return director

# Function to create a movie in the database
def create_movie(session, title, release_year, director_id):
    # Create a new movie object with the provided details
    movie = Movie(title=title, release_year=release_year, director_id=director_id)
    session.add(movie)
    session.commit()
    return movie

# Function to create an actor if they don't already exist in the database
def create_actor(session, actor_name):
    # Query to check the table if the actor already exists by name
    actor = session.query(Actor).filter_by(name=actor_name).first()
    # If actor is not found, create a new one
    if not actor:
        actor = Actor(name=actor_name)
        session.add(actor)
        session.commit()
    return actor

# Function to add a movie to the database
def add_movie():
    # Prompt the user for movie details
    title = input("Enter the movie title: ")
    release_year = input("Enter the release year: ")
    director_name = input("Enter the director's name: ")

    try:
        release_year = int(release_year) # Convert release year to an integer
    except ValueError:
        print("Invalid input for release year. Please enter a valid integer.")
        return # Exit if input is invalid

    # Start a new database session
    session = SessionLocal()
    # Create the director and movie
    director = create_director(session, director_name)
    movie = create_movie(session, title, release_year, director.id)
    # Print confirmation
    print(f"Added movie: {title} (Director: {director_name})")

# Function to add an actor to a movie
def add_actor():
    # Prompt the user for the movie and actor details
    movie_title = input("Enter the movie title: ")
    actor_name = input("Enter the actor's name: ")

    # Start a new database session
    session = SessionLocal()
    # Query the movie table to find the movie by its title
    movie = session.query(Movie).filter_by(title=movie_title).first()
    # If the movie does not exist, print a message and exit
    if not movie:
        print(f"Movie '{movie_title}' not found.")
        return

    # Create actor and associate them with the movie
    actor = create_actor(session, actor_name)
    movie.actors.append(actor) # Add the actor to the movie's list of actors
    session.commit() # Commit the session to save the changes
    # Print confirmation
    print(f"Added actor: {actor_name} to movie: {movie_title}")

# Function to list all movies in database
def list_all_movies():
    session = SessionLocal() # Start a new session
    movies = session.query(Movie).all() # Query all movies in the table
    # Print all movies' details
    for movie in movies:
        print(f"{movie.id}. {movie.title} ({movie.release_year})")

# Function to list all actors in the database
def list_all_actors():
    session = SessionLocal() # Start a new session
    actors = session.query(Actor).all() # Query all actors in the Actor table
    # Print all actors' details
    for actor in actors:
        print(f"{actor.id}. {actor.name}")

# Function to delete a movie by its ID
def delete_movie():
    # Prompt user for the movie ID to delete
    movie_id = input("Enter the movie ID to delete: ")
    try:
        movie_id = int(movie_id) # Convert movie ID to integer
    except ValueError:
        print("Invalid input. Please enter a valid movie ID.")
        return # Exit if input is invalid
    # Start a new session
    session = SessionLocal()
    # Query the Movie table to find the movie by its ID
    movie = session.query(Movie).filter_by(id=movie_id).first()
    if movie:
        session.delete(movie) # Delete the movie from the session
        session.commit() # Commit the session to apply the deletion
        print(f"Deleted movie with ID {movie_id}")
    else:
        print(f"Movie with ID {movie_id} not found.")

# Function to delete an actor by ID
def delete_actor():
    # Prompt user for the actor ID to delete
    actor_id = input("Enter the actor ID to delete: ")
    try:
        actor_id = int(actor_id) # Convert actor ID to integer
    except ValueError:
        print("Invalid input. Please enter a valid actor ID.")
        return # Exit if input is invalid
    # Start a new session
    session = SessionLocal()
    # Query the actor table to find the actor by their ID
    actor = session.query(Actor).filter_by(id=actor_id).first()
    if actor:
        session.delete(actor) # Delete the actor from the session
        session.commit() # Commit the session to apply the deletion
        print(f"Deleted actor with ID {actor_id}")
    else:
        print(f"Actor with ID {actor_id} not found.")

# Main function to interact with the user
def main():
    while True:
        # Print the menu options
        print("\n1. Add Movie")
        print("2. Add Actor to Movie")
        print("3. List All Movies")
        print("4. List All Actors")
        print("5. Delete Movie")
        print("6. Delete Actor")
        print("7. Exit")
        # Prompt the user for their choice
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
            break # Exit the program
        else:
            print("Invalid choice. Please enter 1-7.") # Handle invalid input

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()