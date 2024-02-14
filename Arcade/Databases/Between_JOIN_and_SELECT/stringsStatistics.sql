CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	DECLARE c INT DEFAULT 97;
DROP TABLE IF EXISTS alpha;
CREATE TEMPORARY TABLE alpha (letter VARCHAR(2));

WHILE c <= 122 DO
    INSERT INTO alpha VALUES(CHAR(c));
    SET c = c + 1;
END WHILE;

SELECT 
    letter,
    CHAR_LENGTH(tstring) - CHAR_LENGTH(REPLACE(tstring, letter, '')) AS total,
    (SELECT COUNT(*) FROM strs WHERE INSTR(str, letter) > 0) AS occurrence,
    (SELECT MAX(cnt) FROM (SELECT CHAR_LENGTH(str) - CHAR_LENGTH(REPLACE(str, letter, '')) AS cnt FROM strs) AS sub) AS max_occurrence,
    (SELECT COUNT(*) FROM strs WHERE CHAR_LENGTH(str) - CHAR_LENGTH(REPLACE(str, letter, '')) = (SELECT MAX(cnt) FROM (SELECT CHAR_LENGTH(str) - CHAR_LENGTH(REPLACE(str, letter, '')) AS cnt FROM strs) AS sub)) AS max_occurrence_reached
FROM 
    alpha, (SELECT GROUP_CONCAT(str SEPARATOR '') AS tstring FROM strs) t
HAVING 
    total > 0;


END