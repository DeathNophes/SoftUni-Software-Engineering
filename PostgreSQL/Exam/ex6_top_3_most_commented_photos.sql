SELECT
	ph.id AS "photo_id",
	ph.capture_date,
	ph.description,
	COUNT(com.photo_id) AS "comments_count"
FROM
	photos AS "ph"
JOIN
	comments AS "com"
ON
	ph.id = com.photo_id
WHERE
	ph.description IS NOT NULL
GROUP BY
	ph.id,
	ph.capture_date,
	ph.description
ORDER BY
	comments_count DESC,
	photo_id
LIMIT 3;
