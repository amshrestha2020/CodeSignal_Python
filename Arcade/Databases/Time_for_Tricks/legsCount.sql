DROP PROCEDURE IF EXISTS solution;
CREATE PROCEDURE solution()
    SELECT SUM(CASE WHEN type = 'human' THEN 2 WHEN type IN ('cat', 'dog') THEN 4 ELSE 0 END) as summary_legs
    FROM creatures
    ORDER BY id;
