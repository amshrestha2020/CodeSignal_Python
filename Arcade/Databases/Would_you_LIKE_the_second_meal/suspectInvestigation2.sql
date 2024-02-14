CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id, name, surname
FROM Suspect
WHERE height <= 170 OR NOT (name LIKE 'B%' AND surname LIKE 'Gre_n')
ORDER BY id ASC;


END