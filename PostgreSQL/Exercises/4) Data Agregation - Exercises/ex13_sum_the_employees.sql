SELECT
	COUNT(CASE WHEN department_id = 1 THEN 'Engineering' END)
		AS "Engineering",
	COUNT(CASE WHEN department_id = 2 THEN 'Tool Design' END)
		AS "Tool Design",
	COUNT(CASE WHEN department_id = 3 THEN 'Sales' END)
		AS "Sales",
	COUNT(CASE WHEN department_id = 4 THEN 'Marketing'	END)
		AS "Marketing",
	COUNT(CASE WHEN department_id = 5 THEN 'Purchasing' END)
		AS "Purchasing",
	COUNT(CASE WHEN department_id = 6 THEN 'Research and Development' END)
		AS "Research and Development",
	COUNT(CASE WHEN department_id = 7 THEN 'Production' END)
		AS "Production"
FROM
	employees;
