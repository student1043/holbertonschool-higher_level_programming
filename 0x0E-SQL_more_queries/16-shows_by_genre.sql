-- Task 16: list all shows and genres linked to it
-- Second Line
SELECT tv_shows.title, tv_genres.name FROM tv_shows WHERE tv_genres.name IS NULL LEFT JOIN tv_genres ON name = tv_shows.title ORDER BY title, tv_genres.name ASC;
