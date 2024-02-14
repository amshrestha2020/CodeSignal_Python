CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT package_type, COUNT(*) AS number
FROM (
    SELECT g.id, (
        SELECT package_type
        FROM packages p
        WHERE g.length <= p.length AND g.width <= p.width AND g.height <= p.height
        ORDER BY p.length * p.width * p.height ASC
        LIMIT 1
    ) AS package_type
    FROM gifts g
) t
GROUP BY package_type
ORDER BY package_type ASC;


END