CREATE PROCEDURE solution()
BEGIN
    ALTER TABLE restaurants ADD COLUMN description VARCHAR(100) DEFAULT 'TBD' AFTER name;
    ALTER TABLE restaurants ADD COLUMN active INT DEFAULT 1 AFTER description;

    SELECT * FROM restaurants ORDER BY id;
END

