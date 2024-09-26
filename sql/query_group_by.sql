--query_group_by.sql

SELECT author_id, COUNT(*) AS number_of_books
FROM books
GROUP BY author_id
HAVING COUNT(*) > 1;
