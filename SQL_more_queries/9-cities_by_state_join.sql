-- list all cities contained in the database hbtn_0d_usa
Select cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = id;
