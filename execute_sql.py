import sqlite3
import pathlib

# Define the database file path
db_file_path = pathlib.Path("project.db")

def execute_single_sql_statement(db_path, sql_statement):
    """Execute a single SQL statement."""
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_statement)
            conn.commit()
            print("SQL statement executed successfully.")
    except sqlite3.Error as e:
        print(f"Error executing SQL statement: {e}")

# Define your SQL statement
delete_from_where = """
DELETE FROM books
WHERE title = 'The Lord of the Rings';
"""

# Execute the SQL statement
execute_single_sql_statement(db_file_path, delete_from_where)

def check_books(db_path):
    """Check the contents of the books table."""
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print(f"Error reading from the database: {e}")

# Execute the SQL statement to delete
execute_single_sql_statement(db_file_path, delete_from_where)

# Check the contents of the books table
check_books(db_file_path)

