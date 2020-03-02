-- Task 102: Top 3 cities
SELECT TOP 3 WHERE month = 7 and month = 8 city, AVG(value) as avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
