-- Task 7: New Database
-- Second Line
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT NOT NULL AUTO_INCREMENT, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, PRIMARY KEY (id), CONSTRAINT FK_state_id FOREIGN KEY (state_id) REFERENCES states(id));