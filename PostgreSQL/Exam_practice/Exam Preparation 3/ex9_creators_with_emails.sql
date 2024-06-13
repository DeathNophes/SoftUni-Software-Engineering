SELECT
	CONCAT(cr.first_name, ' ', cr.last_name) AS "full_name",
	cr.email,
	MAX(bg.rating)
FROM
	creators AS "cr"
JOIN
	creators_board_games AS "crbg"
ON
	cr.id = crbg.creator_id
JOIN
	board_games AS "bg"
ON
	crbg.board_game_id = bg.id
WHERE
	cr.email LIKE '%.com'
GROUP BY
	full_name,
	cr.email
ORDER BY
	full_name;
