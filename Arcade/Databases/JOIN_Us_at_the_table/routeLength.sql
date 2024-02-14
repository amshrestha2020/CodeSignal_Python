CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT
    ROUND(SUM(SQRT(POW(c2.x - c1.x, 2) + POW(c2.y - c1.y, 2))), 9) AS total
FROM
    cities c1
JOIN
    cities c2 ON c1.id = c2.id - 1;

END