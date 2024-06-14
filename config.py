import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = 'sqlite:///bank.db,' 

from app import db  # Assuming db.py is in the same directory

if not os.path.exists('bank.db'):
    db.engine.execute("CREATE TABLE sqla_sequence (name VARCHAR PRIMARY KEY)")
    print("Database 'bank.db' created.")