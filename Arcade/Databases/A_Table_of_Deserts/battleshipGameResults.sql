CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT 
    size,
    SUM(IF(hits = 0, 1, 0)) AS undamaged,
    SUM(IF(hits > 0 AND hits < size, 1, 0)) AS partly_damaged,
    SUM(IF(hits = size, 1, 0)) AS sunk
FROM (
    SELECT 
        (bottom_right_x - upper_left_x + 1) * (bottom_right_y - upper_left_y + 1) AS size,
        (SELECT COUNT(*) FROM opponents_shots WHERE target_x BETWEEN upper_left_x AND bottom_right_x AND target_y BETWEEN upper_left_y AND bottom_right_y) AS hits
    FROM 
        locations_of_ships
) AS t
GROUP BY 
    size
ORDER BY 
    size;

END