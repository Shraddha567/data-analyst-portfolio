-- Create Table
-- CREATE TABLE CompanyEmployees (
--     EmployeeID INT PRIMARY KEY,
--     Name VARCHAR(50),
--     Department VARCHAR(50),
--     Salary INT
-- );
-- -- Insert Data
-- INSERT INTO CompanyEmployees (EmployeeID, Name, Department, Salary) VALUES
-- (1, 'Alice', 'HR', 5000),
-- (2, 'Bob', 'IT', 7000),
-- (3, 'Carol', 'IT', 6000),
-- (4, 'Dave', 'HR', 4500),
-- (5, 'Eve', 'Sales', 4000),
-- (6, 'Frank', NULL, 5500),
-- (7, 'Grace', 'Finance', NULL);

-- SELECT Name, Salary,
-- 	CASE 
-- 		WHEN Salary >= 6000 THEN 'High'
-- 		WHEN 4000 <= Salary <= 5999 THEN 'Medium'        
-- 		WHEN Salary IS NULL THEN 'Not Avaialble'
--         Else 'Low'
-- 	END AS SalaryLevel
-- FROM CompanyEmployees;
USE ecom;
-- SELECT * FROM CompanyEmployees;
SELECT Name,
    CASE 
        WHEN Salary IS NULL THEN 'Not Available'
        WHEN Salary >= 6000 THEN 'High'
        WHEN Salary BETWEEN 4000 AND 5999 THEN 'Medium'
        ELSE 'Low' 
    END As SalaryLevel
FROM CompanyEmployees;

