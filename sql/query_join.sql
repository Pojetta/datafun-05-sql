--query_join.sql

SELECT books.title, authors.first, authors.last
FROM books
JOIN authors ON books.author_id = authors.author_id;




