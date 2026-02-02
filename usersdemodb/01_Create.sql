 
CREATE DATABASE usersdemodb;
CREATE TABLE employee (id INT  AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100) UNIQUE NOT Null, gender ENUM('Male', 'Female', 'Other'), 
date_of_birth DATE, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
-- ADD New column in a existing table by using ALTER 
ALTER TABLE employee ADD COLUMN salary DECIMAL(10,2);
select * from employee;
SELECT name, email FROM employee;
-- In (email) field we are using UNIQUE Constraint and we can also Add UNIQUE using ALTER TABLE :
-- ADD CONSTRAINT unique_email UNIQUE (email);
-- For email NOT NULL Constraint Ensures that a column cannot contain NULL values.
RENAME TABLE users TO employee;
RENAME TABLE employee TO users;
-- Filtering Rows with WHERE
-- Equal To - Not Equal To
-- SELECT column1, column2 FROM table_name;
SELECT * FROM users;
SELECT * FROM users WHERE gender = 'Male';
SELECT * FROM users WHERE gender != 'Female';
-- or
SELECT * FROM users WHERE gender <> 'Female';
ALTER TABLE users 