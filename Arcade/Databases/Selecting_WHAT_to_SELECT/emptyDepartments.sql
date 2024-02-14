CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT d.dep_name
    FROM departments d
    LEFT JOIN employees e ON d.id = e.department
    WHERE e.department IS NULL
    ORDER BY d.id;
END