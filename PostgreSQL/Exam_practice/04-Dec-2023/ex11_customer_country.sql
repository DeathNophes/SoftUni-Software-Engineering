CREATE OR REPLACE PROCEDURE
	sp_customer_country_name(
		IN customer_full_name VARCHAR(50),
		OUT country_name VARCHAR(50)
) AS
$$
	BEGIN
		SELECT cou.name INTO country_name
		FROM countries AS "cou"
		JOIN customers AS "c"
		ON cou.id = c.country_id
		WHERE c.first_name || ' ' || c.last_name = customer_full_name;
	END;
$$
LANGUAGE plpgsql;
