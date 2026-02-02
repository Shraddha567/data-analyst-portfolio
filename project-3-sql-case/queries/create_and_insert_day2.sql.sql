-- CREATE DATABASE myDemoDb;
USE myDemoDb;
SELECT * FROM EMPLOYEE;
-- Get all employee names and salaries.
SELECT name, salary FROM EMPLOYEE;
-- Get employees where salary > 50000.
SELECT name, slary FROM employee WHERE salary > 50000;
-- Select employee name as employee_name.

-- Create Table employee whose 
-- id Integer and it should be AUTO_INCREMENT(Constraint), 
-- id should be PRIMARY KEY(Constraint) Unique Key which identifies a record of unique record from a table
-- NOT NULL ensures a column can not be NULL (Constraints) UNIQUE 
-- (AUTO_INCREMENT Automatically generates a unique number for each row)
-- email Should be (VARCHAR datatype) VARCHAR(100) 
-- 100 is a number of character which should be not null , 
-- gender should ENUM ('Male', 'Female', 'Other'),
-- ENUM is a string of object with a value which is used to choose from a permitted values.
-- date_of_birth should be of (date) type data type and it should have 
-- one more field which is created_at TIMESTAMP which is using constraint-
-- (DEFAULT -- CURRENT_TIMESTAMP) 
-- CURRENT_TIMESTAMP is not an SQL constraint itself, 
-- CURRENT_TIMESTAMP is a built-in function that returns the current date and time from the database server.
-- is_active BOOLEAN DEFAULT TRUE