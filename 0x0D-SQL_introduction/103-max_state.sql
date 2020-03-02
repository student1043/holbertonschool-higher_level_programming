-- Task 103: Max by state
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY city ORDER BY max_temp DESC limit 3;
