DROP FUNCTION IF EXISTS response;
CREATE FUNCTION response(name VARCHAR(40)) RETURNS VARCHAR(200) DETERMINISTIC
BEGIN
    DECLARE firstname VARCHAR(20);
    DECLARE lastname VARCHAR(20);
    
    SET firstname = CONCAT(UCASE(LEFT(SUBSTRING_INDEX(name, ' ', 1), 1)), LCASE(SUBSTRING(SUBSTRING_INDEX(name, ' ', 1), 2)));
    SET lastname = CONCAT(UCASE(LEFT(SUBSTRING_INDEX(name, ' ', -1), 1)), LCASE(SUBSTRING(SUBSTRING_INDEX(name, ' ', -1), 2)));
    
    RETURN CONCAT('Dear ', firstname, ' ', lastname, '! We received your message and will process it as soon as possible. Thanks for using our service. FooBar On! - FooBarIO team.');
END;

CREATE PROCEDURE solution()
BEGIN
    SELECT id, name, response(name) AS response
    FROM customers;
END;

