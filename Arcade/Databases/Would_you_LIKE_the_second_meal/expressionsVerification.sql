CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id, a, b, operation, c
FROM expressions
WHERE
  (operation = '+' AND a + b = c)
  OR (operation = '-' AND a - b = c)
  OR (operation = '*' AND a * b = c)
  OR (operation = '/' AND b != 0 AND a / b = c)
ORDER BY id;

END