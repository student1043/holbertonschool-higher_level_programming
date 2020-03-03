-- Task 13: Show count
-- Second Line
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre.id) AS number_of_shows FROM tv_show_genres WHERE tv_show_genres.genre.id IS NOT NULL ORDER BY number_of_shows;
