-- file: 9-full_creation.sql
-- description: creating a table with multiple rows

-- script that creates a table with multiple rows
CREATE TABLE IF NOT EXISTS second_table (id INTEGER AUTO_INCREMENT, name VARCHAR(256), score INTEGER);

INSERT INTO second_table (name, score) VALUES (('John', 10), ('Alex', 3), ('Bob', 14), ('George', 8));
