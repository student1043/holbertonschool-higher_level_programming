-- Task 9: all cities and states
-- Second Line
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state.id=states.id ORDER BY cities.id ASC;
