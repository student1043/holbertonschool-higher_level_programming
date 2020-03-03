-- Task 14: Dexter
-- Second Line
USE hbtn_0d_tvshows;
SELECT tv_genres.name AS name FROM tv_genres WHERE name= (SELECT name FROM tv_shows.title WHERE name='Dexter') INNER JOIN tv_show_genres ON tv_genres.id=tv_show_genres.genre_id GROUP BY name ORDER BY name ASC;
