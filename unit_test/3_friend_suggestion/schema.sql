-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS persons;

CREATE TABLE persons (
  id   INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL
);

INSERT INTO persons (id, name)
VALUES (NULL, 'Ali'), (NULL, 'Babak'), (NULL, 'Mina'), (NULL, 'Zeynab'), (NULL, 'Raha'), (NULL, 'Khadijeh')