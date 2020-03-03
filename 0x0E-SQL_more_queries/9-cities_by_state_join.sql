-- Task 9: all cities and states
-- Second Line
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state.id=states.id ORDER BY id ASC;
