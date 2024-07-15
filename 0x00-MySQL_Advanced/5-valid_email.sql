-- creates a trigger that resets the attribute valid_email only when the email has been changed
DROP TRIGGER IF EXISTS reset_validate_email;

DELIMITER $$

-- Create a new trigger
CREATE TRIGGER reset_validate_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET valid_email = 0;
    END IF;
END $$

DELIMITER ;
