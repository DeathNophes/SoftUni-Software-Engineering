CREATE OR REPLACE FUNCTION
	fn_creator_with_board_games(
		first_name_of_creator VARCHAR(30)
) RETURNS INT
AS
$$
	BEGIN
		RETURN(
			SELECT COUNT(bg.id)
			FROM board_games AS "bg"
			JOIN creators_board_games AS "crbg"
			ON bg.id = crbg.board_game_id
			JOIN creators AS "cr"
			ON crbg.creator_id = cr.id
			WHERE cr.first_name = first_name_of_creator);
	END;
$$
LANGUAGE plpgsql;
