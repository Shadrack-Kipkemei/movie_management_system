import click
from database.connection import SessionLocal
from models.movie import Movie
from models.actor import Actor
from models.director import Director


# Create CLI group
@click.group()
def cli():
    pass

# Command to add a movie
@click.command()
@click.argument('title')
@click.argument('release_year')
@click.argument('director_name')
def add_movie(title, release_year, director_name):
    session = SessionLocal()
    # Find or create director
    director = session.query(Director). filter_by(name = director_name).first()
    if not director:
        director = Director(name = director_name)
        session.add(director)
        session.commit()

    # Create and add movie
    new_movie = Movie(title = title, release_year = release_year, director_id = director.id)
    session.add(new_movie)
    session.commit()
    print(f"Added movie: {title} (Director: {director_name})")

# Command to add an actor to a movie
@click.command()
@click.argument('title')
@click.argument('actor_name')
def add_actor(title, actor_name):
    session = SessionLocal()

    # Find movie and actor
    movie = session.query(Movie).filter_by(title = title).first()
    actor = session.query(Actor).filter_by(name = actor_name).first()
    if not actor:
        actor = Actor(name = actor_name)
        session.add(actor)
        session.commit()

    # Add actor and movie
    movie.actors.append(actor)
    session.commit()
    print(f"Added actor: {actor_name} to movie: {title}")

cli.add_command(add_movie)
cli.add_command(add_actor)

if __name__ == "__main__":
    cli()