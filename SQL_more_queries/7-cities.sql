-- Creates the database hbtn_0d_usa and the table cities
-- cities
-- 
-- id int, unique, autogenered, cant be null, primary key
-- name varchar(256) not null
-- state_id int, cant be null, foreing key, references to id of the states

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY, state_id INT NOT NULL, FOREIGN KEY(state_id) REFERENCES states(id), name varchar(256) NOT NULL);
