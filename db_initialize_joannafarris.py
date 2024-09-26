"""
db_initialize.joannafarris.py: Database Initialization Script

This script is responsible for setting up the SQLite database for the datafun-05-sql project. It performs the following tasks:
1. Verifies the existence of required directories and creates them if needed.
2. Creates the SQLite database file.
3. Creates necessary database tables by executing SQL statements.
4. Inserts initial data into the tables from CSV files.

Usage:
Run this script first to initialize the database and populate it with initial data.

Functions:
- `verify_and_create_folders(paths)`: Ensures required directories exist.
- `create_database(db_path)`: Creates the SQLite database file.
- `create_tables(db_path, sql_file_path)`: Creates database tables using SQL statements.
- `insert_data_from_csv(db_path, author_data_path, book_data_path)`: Populates the tables with data from CSV files.
"""

# Import from Python Standard Library 
import sqlite3
import pathlib
import logging

# Import from external packages (requires virtual environment)
import pandas as pd

###############################
# Logging Configuration
###############################
# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='initialize_log.txt', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    filemode='a')

###############################
# File Paths
###############################
# Define paths using joinpath
db_file_path = pathlib.Path("project.db")
sql_file_path = pathlib.Path("sql").joinpath("create_tables.sql")
author_data_path = pathlib.Path("data").joinpath("authors.csv")
book_data_path = pathlib.Path("data").joinpath("books.csv")

###############################
# Define Functions
###############################

def verify_and_create_folders(paths):
    """Verify and create folders if they don't exist."""
    for path in paths:
        folder = path.parent
        if not folder.exists():
            folder.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created folder: {folder}")
            print(f"Created folder: {folder}")
        else:
            logging.info(f"Folder already exists: {folder}")
            print(f"Folder already exists: {folder}")

def create_database(db_path):
    """Create a new SQLite database file if it doesn't exist."""
    try:
        conn = sqlite3.connect(db_path)
        conn.close()
        logging.info(f"Database created successfully at {db_path}")
        print("Database created successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error creating the database: {e}")
        print(f"Error creating the database: {e}")

def create_tables(db_path, sql_file_path):
    """Read and execute SQL statements to create tables."""
    try:
        with sqlite3.connect(db_path) as conn:
            with open(sql_file_path, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Tables created successfully using {sql_file_path}")
            print("Tables created successfully.")
    except sqlite3.Error as e:
        logging.error(f"Error creating tables: {e}")
        print(f"Error creating tables: {e}")

def insert_data_from_csv(db_path, author_data_path, book_data_path):
    """Read data from CSV files and insert the records into their respective tables."""
    try:
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_path) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            logging.info(f"Data inserted successfully from {author_data_path} and {book_data_path}")
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        logging.error(f"Error inserting data: {e}")
        print(f"Error inserting data: {e}")

def main():
    paths_to_verify = [sql_file_path, author_data_path, book_data_path]
    verify_and_create_folders(paths_to_verify)   

    create_database(db_file_path)
    create_tables(db_file_path, sql_file_path)
    insert_data_from_csv(db_file_path, author_data_path, book_data_path)

if __name__ == "__main__":
    main()
