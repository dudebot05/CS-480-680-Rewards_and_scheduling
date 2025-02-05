from sqlalchemy import create_engine
import pymysql

# MySQL connection details
user = 'root'  # MySQL username
password = 'root'  # MySQL password
host = 'localhost'  # Address of the MySQL server (localhost for a local setup)
database = 'loyals_database'  # Name of the database we're working with

# Connection string to MySQL (connecting to the 'mysql' database temporarily)
connection_string = f'mysql+pymysql://{user}:{password}@{host}/mysql'

# Set up the engine to connect to MySQL
engine = create_engine(connection_string)

# Try creating the database if it doesn't already exist
try:
    with engine.connect() as connection:
        # Run the query to create the database if it doesn't exist yet
        connection.execute(f"CREATE DATABASE IF NOT EXISTS {database};")
        print(f"Database '{database}' has been created or already exists.")
except Exception as e:
    print(f"An error occurred: {e}")
