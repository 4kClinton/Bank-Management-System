from sqlalchemy import create_engine
from app.models import Base
from config import DATABASE_URI

# Create an SQLite engine
engine = create_engine(DATABASE_URI)

# Create all tables
Base.metadata.create_all(engine)

print("Database initialized!")

