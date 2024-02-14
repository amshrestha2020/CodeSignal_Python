CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT 
        TABLE_NAME AS tab_name,
        COLUMN_NAME AS col_name,
        DATA_TYPE AS data_type
    FROM 
        INFORMATION_SCHEMA.COLUMNS
    WHERE 
        TABLE_NAME LIKE 'e%s' AND
        TABLE_SCHEMA = 'ri_db'
    ORDER BY 
        tab_name, col_name;
END
