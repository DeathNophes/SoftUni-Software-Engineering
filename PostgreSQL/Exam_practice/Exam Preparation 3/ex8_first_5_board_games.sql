SELECT
	bg.name,
	bg.rating,
	cat.name AS "category_name"
FROM
	board_games AS "bg"
JOIN
	categories AS "cat"
ON
	bg.category_id = cat.id
JOIN
	players_ranges AS "pr"
ON
	bg.players_range_id = pr.id
WHERE
	bg.rating > 7.00
		AND
	(bg.name LIKE '%a%' OR bg.name LIKE '%A%') OR bg.rating >= 7.50
		AND
	pr.max_players <= 5
		AND
	pr.min_players >= 2
ORDER BY
	bg.name,
	bg.rating DESC
LIMIT 5;
