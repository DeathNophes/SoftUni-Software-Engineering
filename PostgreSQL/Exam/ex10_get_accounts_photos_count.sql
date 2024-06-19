CREATE OR REPLACE FUNCTION
	udf_accounts_photos_count(
		account_username VARCHAR(30)
) RETURNS INT
AS
$$
	DECLARE photos_count INT;
	BEGIN
		SELECT COUNT(ph.id) INTO photos_count
		FROM photos AS "ph"
		JOIN accounts_photos AS "ap"
		ON ph.id = ap.photo_id
		JOIN accounts AS "a"
		ON ap.account_id = a.id
		WHERE a.username = account_username;
		RETURN photos_count;
	END;
$$
LANGUAGE plpgsql;
