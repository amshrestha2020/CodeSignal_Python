CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT ae.id, 
       CASE 
           WHEN SUM(ep.expenditure_sum) <= ae.value THEN 0 
           ELSE SUM(ep.expenditure_sum) - ae.value 
       END AS loss
FROM expenditure_plan ep
JOIN allowable_expenditure ae ON WEEK(ep.monday_date, 1) BETWEEN ae.left_bound AND ae.right_bound
GROUP BY ae.id
ORDER BY ae.id;
END

