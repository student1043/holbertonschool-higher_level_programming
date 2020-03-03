-- Task 9: all cities and states
-- Second Line
SELECT id, name, states.name FROM cities WHERE state_id= (SELECT id FROM states) ORDER BY id ASC;
