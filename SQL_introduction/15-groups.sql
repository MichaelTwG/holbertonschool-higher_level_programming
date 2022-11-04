-- List the number of records with the same score in the table
-- display the score and number
-- the list should be sorted bby number of records DESC
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score;
