-- List all cities of Califonia that can be found in database hbtn_0d_usa
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states where name = 'California');
