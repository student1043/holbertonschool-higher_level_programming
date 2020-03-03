-- Task 8: List all cities of California
-- Second Line
SELECT id, name FROM cities WHERE state_id= (SELECT id FROM states WHERE name='California') ORDER BY id ASC;
