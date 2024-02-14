CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT holiday_date AS ski_date
    FROM holidays
    WHERE holiday_date IN (SELECT sunny_date FROM weather)
    ORDER BY holiday_date;
END