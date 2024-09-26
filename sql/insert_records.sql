--insert_records.sql

INSERT INTO authors (author_id, first, last) VALUES 
('b3f1e60c-2078-46af-b2ec-50f66d0e0f3c', 'Ernest', 'Hemingway'),
('a23e9f88-f7b8-4a11-91c5-25b5b3db6e9a', 'Agatha', 'Christie'),
('c29c5ff2-12f1-4e62-93c2-bb2b63b7eb7a', 'Stephen', 'King'),
('ebce78bb-4f1a-4f38-bec5-29982e75e22a', 'Isaac', 'Asimov'),
('f1e03b0e-e108-4654-bb05-72f6b1f83e3a', 'Toni', 'Morrison'),
('81ab4e48-0e69-4a92-b1cc-c12b29bb2783', 'Gabriel', 'Garcia Marquez'),
('64e69d2c-5a99-4a06-8a48-b441e890f6f1', 'Cormac', 'McCarthy'),
('bc7eacec-e5ae-4c94-96a2-50a54249e5cf', 'John', 'Steinbeck'),
('9a17d75f-8c24-4e2b-8b0b-daa3c907e9e5', 'Mark', 'Twain'),
('57c6a8f7-e5ef-4913-8450-0c0456c13244', 'Virginia', 'Woolf');

INSERT INTO books (book_id, title, year_published, author_id) VALUES 
('b1237d56-d1f8-4f74-8be2-d712764ae8bc', 'The Old Man and the Sea', 1952, 'b3f1e60c-2078-46af-b2ec-50f66d0e0f3c'),
('a54a3c1b-9ff5-4781-a2ef-e9e14a325c5a', 'Murder on the Orient Express', 1934, 'a23e9f88-f7b8-4a11-91c5-25b5b3db6e9a'),
('f89c6d1d-0b3f-4c35-8bc6-7f4b27f3d32e', 'The Shining', 1977, 'c29c5ff2-12f1-4e62-93c2-bb2b63b7eb7a'),
('efb9f2d3-dc89-4c1e-a8b5-d28dba9e084f', 'Foundation', 1951, 'ebce78bb-4f1a-4f38-bec5-29982e75e22a'),
('4a06a7c7-b575-4316-bb61-c2042f9e5b18', 'Beloved', 1987, 'f1e03b0e-e108-4654-bb05-72f6b1f83e3a'),
('9a1b5e39-9964-471e-8ec1-428c53be1d4e', 'No Country for Old Men', 2005, '81ab4e48-0e69-4a92-b1cc-c12b29bb2783'),
('a5c8ebeb-4330-4eaf-b81d-91f3ef206982', 'East of Eden', 1952, '64e69d2c-5a99-4a06-8a48-b441e890f6f1'),
('d03f24e8-55e7-4f00-8c9f-4bda3b774b62', 'The Grapes of Wrath', 1939, 'bc7eacec-e5ae-4c94-96a2-50a54249e5cf'),
('a23c78d7-97ec-4932-9019-f17ab541cfd2', 'The Adventures of Tom Sawyer', 1876, '9a17d75f-8c24-4e2b-8b0b-daa3c907e9e5'),
('c74a4c7b-429b-4d82-8c5f-d96aa8e1788f', 'Mrs. Dalloway', 1925, '57c6a8f7-e5ef-4913-8450-0c0456c13244');


