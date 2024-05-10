SELECT
	title,
	ROUND(cost, 3) AS "modified_price"
    --> We can also use TRUNC()
FROM
	books
ORDER BY
	id;
