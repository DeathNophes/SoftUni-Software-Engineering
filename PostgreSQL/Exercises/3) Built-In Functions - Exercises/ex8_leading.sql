SELECT
	continent_name,
	TRIM(LEADING FROM continent_name) AS "trim"
    --> Remove leading spaces from the continent_name
FROM
	continents;
