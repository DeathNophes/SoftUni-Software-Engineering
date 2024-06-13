SELECT
	name,
	ROUND(rating, 2)
FROM
	board_games
ORDER BY
	release_year ASC,
	name DESC;
