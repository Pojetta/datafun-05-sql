--update_records.sql

UPDATE books 
SET publication_year = 2000 
WHERE title = 'Harry Potter and the Sorcerer\'s Stone';

UPDATE authors 
SET birth_year = 1893 
WHERE name = 'J.R.R. Tolkien';

