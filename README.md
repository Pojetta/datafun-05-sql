# datafun-05-sql

## Project 5: Database Management with Python and SQLite

### Overview
Project 5 focuses on the creation and management of a database using Python and SQL, emphasizing interactions with the database through SQLite. This project includes two primary scripts: `db_initialize.joannafarris.py` and `db_operations.joannafarris.py`, which work together to set up the database and perform various operations.

### Commands Used When Setting Up Project
To set up the project, run the following commands:

```zsh
git clone <your repo URL>  
git add .  
git commit -m "descriptive commit message"  
git push -u origin main  
python3 -m venv .venv  
source .venv/bin/activate  
python3 -m pip install -r requirements.txt  
```

### db_initialize.joannafarris.py
This script is responsible for setting up the database. It verifies the existence of required directories, creates the database, and populates the tables with initial data from CSV files.

**Key Functions:**
- `verify_and_create_folders(paths)`: Checks and creates necessary directories.
- `create_database(db_path)`: Creates the SQLite database file.
- `create_tables(db_path, sql_file_path)`: Reads and executes SQL statements to create tables.
- `insert_data_from_csv(db_path, author_data_path, book_data_path)`: Reads data from CSV files and inserts records into the database tables.

### db_operations.joannafarris.py
This script executes various SQL operations defined in separate SQL files. It performs tasks such as updating records, deleting records, and executing queries.

**Key Functions:**
- `execute_sql_from_file(db_file_path, sql_file)`: Executes SQL commands from a specified SQL file.
