SELECT
	cr.id,
	CONCAT(cr.first_name, ' ', cr.last_name) AS "creator_name",
	cr.email
FROM
	creators AS "cr"
LEFT JOIN
	creators_board_games AS "crbg"
ON
	crbg.creator_id = cr.id
WHERE
	crbg.board_game_id IS NULL
ORDER BY
	creator_name;
