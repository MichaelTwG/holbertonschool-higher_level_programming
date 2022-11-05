-- Create a table unique_id
-- id int, default 1, unique value
-- name varchar(256)
CREATE TABLE IF NOT EXISTS unique_id
 (id int DEFAULT 1 UNIQUE, name varchar(256));
