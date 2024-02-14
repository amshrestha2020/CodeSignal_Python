CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT DISTINCT
    LEAST(s1.name, s2.name) AS place1,
    GREATEST(s1.name, s2.name) AS place2
FROM sights s1
JOIN sights s2 ON s1.id < s2.id
WHERE SQRT(POW(s1.x - s2.x, 2) + POW(s1.y - s2.y, 2)) < 5
ORDER BY place1, place2;

END