CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT 
  ROUND(ST_AREA(ST_CONVEXHULL(ST_COLLECT(POINT(x, y)))), 1) AS area
FROM 
  places;

END