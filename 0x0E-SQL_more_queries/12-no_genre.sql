-- Task 12: no genre linked
-- Second line
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows WHERE tv_show_genres.genre_id IS NULL ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
