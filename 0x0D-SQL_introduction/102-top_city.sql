-- Task 102: Top 3 cities
SELECT TOP 3 city, AVG(value) as avg_temp FROM temperatures WHERE (month = 7 and month = 8) GROUP BY city ORDER BY avg_temp DESC;
