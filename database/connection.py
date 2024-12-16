from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Database URL
DATABASE_URL = 'sqlite3:///movies.db'

# Create engine and sessionmaker
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)