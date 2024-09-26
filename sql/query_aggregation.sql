-- query_aggregation.sql

SELECT author_id, COUNT(*) AS number_of_books
FROM books
GROUP BY author_id;