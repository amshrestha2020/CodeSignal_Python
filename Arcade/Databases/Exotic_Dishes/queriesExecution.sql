CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    DECLARE done INT DEFAULT 0;
    DECLARE query_name_var VARCHAR(100);
    DECLARE query_code_var TEXT;
    DECLARE query_result VARCHAR(100);

    -- Declare cursor to iterate over queries
    DECLARE cur CURSOR FOR SELECT query_name, code FROM queries;
    
    -- Declare continue handler to exit loop when no more rows
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
	
	DROP TEMPORARY TABLE IF EXISTS report;

    -- Create temporary table to store report values
    CREATE TEMPORARY TABLE IF NOT EXISTS report (
        query_name VARCHAR(100),
        val VARCHAR(100)
    );

    -- Open cursor
    OPEN cur;
    read_loop: LOOP
      FETCH cur INTO query_name_var, query_code_var;
      IF done THEN
        LEAVE read_loop;
      END IF;

      SET @execq=CONCAT("INSERT INTO report values(", "'", query_name_var, "'", ",(", query_code_var, "));");

      PREPARE stmt FROM @execq;
      EXECUTE stmt; 
      DEALLOCATE PREPARE stmt;
    END LOOP;
    CLOSE cur;
    
    SELECT query_name, val FROM report;
END

