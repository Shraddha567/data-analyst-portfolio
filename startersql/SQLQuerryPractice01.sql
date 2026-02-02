-- CREATE DATABASE startersql;
USE startersql;
-- CREATE TABLE users (
-- id INT AUTO_INCREMENT PRIMARY KEY,
-- name VARCHAR(100) NOT NULL,
-- email VARCHAR(100) UNIQUE NOT NULL,
-- gender ENUM('Male', 'Female', 'Other'),
-- date_of_birth DATE,
-- created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
-- DROP DATABASE startersql;

-- INSERT  INTO users VALUES('1', 'Alice', 'alice@example.com', 'Female',  '1995-05-14', DEFAULT);
-- RENAME TABLE users TO employee;
-- RENAME TABLE employee TO users
-- ALTER TABLE users ADD COLUMN is_Active BOOLEAN DEFAULT TRUE;
-- ALTER TABLE users DROP COLUMN is_active;
-- ALTER TABLE users MODIFY COLUMN email VARCHAR(100) FIRST;
-- ALTER TABLE users MODIFY COLUMN email VARCHAR(100) AFTER id;

-- ALTER TABLE users ADD COLUMN Salary Decimal(10,2);
-- ALTER TABLE users MODIFY COLUMN Salary DECIMAL(10,2) NOT NULL DEFAULT 0.00  AFTER name;
-- ALTER TABLE users MODIFY COLUMN Salary DECIMAL(10,2) NOT NULL DEFAULT 0.00 AFTER created_at;

-- UPDATE users SET Salary=10000 WHERE id=1;

-- SELECT * FROM users WHERE date_of_birth IS NULL;
-- SELECT * FROM users WHERE date_of_birth IS NOT NULL;
SELECT * from users WHERE gender in ('Male', 'Female');


