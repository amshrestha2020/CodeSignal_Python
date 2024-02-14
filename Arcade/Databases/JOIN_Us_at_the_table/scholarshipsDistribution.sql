CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT DISTINCT c.candidate_id AS student_id
FROM candidates c
LEFT JOIN detentions d ON c.candidate_id = d.student_id
WHERE d.student_id IS NULL
ORDER BY c.candidate_id;


END