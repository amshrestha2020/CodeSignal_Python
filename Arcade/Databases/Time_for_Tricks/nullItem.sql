CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT COUNT(*) AS number_of_nulls
FROM departments
WHERE 
    description IS NULL OR 
    UPPER(TRIM(description)) IN ('NULL', 'NIL', '-');

END