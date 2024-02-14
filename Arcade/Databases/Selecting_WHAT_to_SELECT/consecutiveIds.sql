CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id AS oldId, ROW_NUMBER() OVER (ORDER BY id) AS newId
    FROM itemIds
    ORDER BY newId;
END