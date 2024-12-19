## Movie Management System

Date, 2024/12/18 By ***Shadrack Kipkemei***

A simple command-line movie management system built with SQLAlchemy, which allows users to manage movies, actors, and directors in a relational database. The system supports operations such as adding, listing, and deleting movies, actors, and directors, as well as associating actors with movies.

## Features

* Add Movies: Create new movie records with details such as title, release year, and director.
* Add Actors to Movies: Link actors to movies by adding actors to specific movie records.
* List Movies and Actors: View all movies and actors in the system.
* Delete Movies and Actors: Remove movies and actors from the system.
* Create Directors: Add new directors if they don't already exist in the database.

## Technologies Used

* SQLAlchemy: ORM for database interaction.
* SQLite (or any other database configured with SQLAlchemy): Stores data about movies, actors, and directors.
* Python: Core language for implementing the application logic.

## Requirements

* Python 3.x
* SQLAlchemy
* SQLite (or any SQL database supported by SQLAlchemy)

## Installation
Follow these steps to set up the project on your local machine:
1. Clone the repository:
```
git clone https://github.com/yourusername/movie-management-system.git
cd movie-management-system
```
2. Create a Virtual Environment

```pipenv install```

3. Activate the Virtual Environment

```pipenv shell```

4. Install dependencies
You can install the required Python packages using pip:

```pip install sqlalchemy```

## Database Setup

This system assumes you already have a configured database using SQLAlchemy. The models for movies, actors, and directors are defined using SQLAlchemy ORM. The SessionLocal object is used to handle interactions with the database.

To use this system, simply create the tables using the appropriate Base.metadata.create_all() method to ensure the database schema is created.

## Models Overview

# Actor Model

* Attributes:

    * id: Primary key
    * name: Name of the actor

* Relationships:

    * Many-to-many relationship with the Movie model through the movie_actors association table.

# Director Model
* Attributes:

    * id: Primary key
    * name: Name of the director

* Relationships:

    * One-to-many relationship with the Movie model.

# Movie Model
* Attributes:

    * id: Primary key
    * title: Title of the movie
    * release_year: Release year of the movie
    * director_id: Foreign key reference to the Director model
* Relationships:

    * Many-to-one relationship with the Director model.
    * Many-to-many relationship with the Actor model via the movie_actors association table.

# Association Table: movie_actors
* Links movies and actors in a many-to-many relationship.
    * movie_id: Foreign key to the Movie model
    * actor_id: Foreign key to the Actor model

## Running the Application
To run the application, execute the cli.py file. This file provides a command-line interface to manage the movies, actors, and directors in the database.

```python cli.py```

# Available Commands:
1. Add Movie: Adds a new movie along with the director.
2. Add Actor to Movie: Adds an actor to an existing movie.
3. List All Movies: Lists all movies stored in the database.
4. List All Actors: Lists all actors stored in the database.
5. Delete Movie: Deletes a movie by its ID.
6. Delete Actor: Deletes an actor by their ID.
7. Exit: Exit the application.

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request. To contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make the necessary changes and commit them.
4. Push the changes to your fork.
5. Create a pull request with a detailed description of your changes.

## License

The content of this project is licensed under the MIT license Copyright (c) 2024.

