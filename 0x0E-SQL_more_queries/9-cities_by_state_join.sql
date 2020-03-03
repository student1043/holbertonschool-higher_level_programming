-- Task 9: all cities and states
-- Second Line
USE hbtn_0d_usa;
SELECT cities.id,cities.name,states.name FROM cities LEFT JOIN states ON cities.state.id=states.id ORDER BY id ASC;
