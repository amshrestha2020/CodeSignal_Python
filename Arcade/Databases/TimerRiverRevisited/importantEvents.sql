CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT id, name, event_date, participants
FROM events
ORDER BY 
  CASE 
    WHEN DAYOFWEEK(event_date) = 1 THEN 8
    ELSE DAYOFWEEK(event_date)
  END,
  participants DESC;

END