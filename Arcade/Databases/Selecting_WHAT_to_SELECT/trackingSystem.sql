CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT t.anonymous_id AS anonym_id,
           t1.event_name AS last_null,
           t2.event_name AS first_notnull
    FROM (
        SELECT anonymous_id
        FROM tracks
        GROUP BY anonymous_id
    ) AS t
    LEFT JOIN (
        SELECT anonymous_id, 
               MAX(received_at) AS max_received_at
        FROM tracks
        WHERE user_id IS NULL
        GROUP BY anonymous_id
    ) AS t_null ON t.anonymous_id = t_null.anonymous_id
    LEFT JOIN (
        SELECT anonymous_id,
               MIN(received_at) AS min_received_at
        FROM tracks
        WHERE user_id IS NOT NULL
        GROUP BY anonymous_id
    ) AS t_notnull ON t.anonymous_id = t_notnull.anonymous_id
    LEFT JOIN tracks AS t1 ON t_null.anonymous_id = t1.anonymous_id AND t_null.max_received_at = t1.received_at
    LEFT JOIN tracks AS t2 ON t_notnull.anonymous_id = t2.anonymous_id AND t_notnull.min_received_at = t2.received_at
    ORDER BY t.anonymous_id;
END