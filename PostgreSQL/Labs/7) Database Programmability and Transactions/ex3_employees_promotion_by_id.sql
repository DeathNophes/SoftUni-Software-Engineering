CREATE PROCEDURE sp_increase_salary_by_id(id INT)
AS
$$
    BEGIN
        IF (SELECT employee_id FROM employees WHERE employee_id = id) IS NULL THEN
            RETURN; -- We can also use ROLLBACK here
        ELSE
            UPDATE employees SET salary = salary * 1.05 WHERE employee_id = id;
        END IF;
        COMMIT; -- This is done automatically
    END;
$$
LANGUAGE plpgsql;
