SELECT
	department_id,
	COUNT(department_id)
    --> COUNT(*) would also get the job done here
FROM
	employees
GROUP BY
	department_id
ORDER BY
	department_id;
