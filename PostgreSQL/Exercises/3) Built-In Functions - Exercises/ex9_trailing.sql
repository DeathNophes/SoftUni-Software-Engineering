SELECT
	continent_name,
	TRIM(TRAILING FROM continent_name) AS "trim"
    --> Remove trailing spaces from the continent_name
FROM
	continents;
