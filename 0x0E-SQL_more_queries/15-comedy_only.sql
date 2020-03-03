-- Task 15: Only comedy
-- Second Line
SELECT title FROM tv_shows LEFT JOIN tv_genres ON id = tv_show_genres.genre_id LEFT JOIN tv_show_genres ON show_id = tv_shows.id WHERE title = 'Comedy' ORDER BY title ASC;
