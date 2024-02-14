CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT 
  CONCAT(
    CASE WHEN gender = 'M' THEN 'King ' ELSE 'Queen ' END,
    name
  ) AS name
FROM 
  Successors
ORDER BY 
  birthday;

END