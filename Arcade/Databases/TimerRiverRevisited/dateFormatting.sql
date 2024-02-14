CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT Date(date_str) AS date_iso
    FROM documents
    ORDER BY id;

END