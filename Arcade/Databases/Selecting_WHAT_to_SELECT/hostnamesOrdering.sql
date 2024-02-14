CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id, hostname
    FROM hostnames
    ORDER BY 
      SUBSTRING_INDEX(CONCAT(' .',hostname), '.', -1),
      SUBSTRING_INDEX(CONCAT(' ..',hostname), '.', -2),
	  hostname ASC;
END