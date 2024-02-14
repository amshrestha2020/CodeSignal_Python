CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT
    COUNT(*) AS number,
    AVG(population) AS average,
    SUM(population) AS total
FROM countries;

END