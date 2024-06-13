SELECT
	bg.id,
	bg.name,
	bg.release_year,
	cat.name
FROM
	board_games AS "bg"
JOIN
	categories AS "cat"
ON
	bg.category_id = cat.id
WHERE
	cat.name IN ('Strategy Games', 'Wargames')
ORDER BY
	bg.release_year DESC;
