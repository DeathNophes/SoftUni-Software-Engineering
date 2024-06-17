UPDATE coaches
SET salary = salary * coach_level
WHERE (
	SELECT COUNT(pc.player_id)
	FROM coaches AS "c"
	JOIN players_coaches AS "pc"
	ON c.id = pc.coach_id
	WHERE c.first_name LIKE 'C%'
	) > 1;
