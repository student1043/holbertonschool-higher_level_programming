-- Task 15: list all records with the same score
SELECT COUNT(score) as number FROM second_table GROUP BY score ORDER BY number DESC;
