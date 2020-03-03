-- Task 16: list all shows and genres linked to it
-- Second Line
SELECT tv_shows.title, tv_genres.name FROM tv_shows LEFT JOIN tv_genres ON name = tv_shows.title LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY title, tv_genres.name ASC;
