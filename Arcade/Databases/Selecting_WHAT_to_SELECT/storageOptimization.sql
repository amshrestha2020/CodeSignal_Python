CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id, 'name' AS column_name, CAST(name AS CHAR) AS value FROM workers_info WHERE name IS NOT NULL
    UNION ALL
    SELECT id, 'date_of_birth' AS column_name, DATE_FORMAT(date_of_birth, '%Y-%m-%d') AS value FROM workers_info WHERE date_of_birth IS NOT NULL
    UNION ALL
    SELECT id, 'salary' AS column_name, CAST(salary AS CHAR) AS value FROM workers_info WHERE salary IS NOT NULL
    ORDER BY id, 
             CASE 
                 WHEN column_name = 'name' THEN 1
                 WHEN column_name = 'date_of_birth' THEN 2
                 WHEN column_name = 'salary' THEN 3
             END;
END