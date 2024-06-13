SELECT
	a.name AS "address",
	CASE
		WHEN EXTRACT(HOUR FROM co.start) BETWEEN 6 AND 20 THEN 'Day'
		ELSE 'Night'
	END AS "day_time",
	co.bill,
	cl.full_name,
	cr.make,
	cr.model,
	cat.name AS "category_name"
FROM
	clients AS "cl"
JOIN
	courses AS "co"
ON
	cl.id = co.client_id
JOIN
	addresses AS "a"
ON
	co.from_address_id = a.id
JOIN
	cars AS "cr"
ON
	co.car_id = cr.id
JOIN
	categories AS "cat"
ON
	cr.category_id = cat.id
ORDER BY
	co.id;
