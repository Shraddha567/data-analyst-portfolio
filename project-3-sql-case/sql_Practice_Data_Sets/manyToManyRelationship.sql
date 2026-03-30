-- Write an SQL query to list all the restaurants in Bangalore that serve "Pizza" cuisine and have a rating greater than 4.
-- Columns to be Returned:
-- RestaurantName — The name of the restaurant.
-- CuisineName — The name of the cuisine offered.
-- Rating — The rating of the restaurant.

-- -- Create the tables
-- CREATE TABLE restaurants (
--     RestaurantID INT PRIMARY KEY,
--     RestaurantName VARCHAR(255),
--     CountryCode CHAR(2),
--     City VARCHAR(100),
--     Address VARCHAR(255),
--     Locality VARCHAR(255),
--     LocalityVerbose VARCHAR(255),
--     Currency VARCHAR(10),
--     Price_range INT,
--     Average_Cost_for_two INT,
--     Votes INT,
--     Rating FLOAT
-- );

-- CREATE TABLE restaurant_features (
--     RestaurantID INT,
--     Has_Table_booking BOOLEAN,
--     Has_Online_delivery BOOLEAN,
--     Is_delivering_now BOOLEAN,
--     Switch_to_order_menu BOOLEAN,
--     FOREIGN KEY (RestaurantID) REFERENCES restaurants(RestaurantID)
-- );

-- CREATE TABLE cuisines (
--     CuisineID INT PRIMARY KEY,
--     CuisineName VARCHAR(255)
-- );

-- CREATE TABLE restaurant_cuisines (
--     RestaurantID INT,
--     CuisineID INT,
--     FOREIGN KEY (RestaurantID) REFERENCES restaurants(RestaurantID),
--     FOREIGN KEY (CuisineID) REFERENCES cuisines(CuisineID)
-- );

-- Write your code here
-- SELECT r.RestaurantName, c.CuisineName, r.Rating
-- FROM restaurants r
-- JOIN restaurant_cuisines rc
-- ON r.RestaurantID = rc.RestaurantID
-- JOIN cuisines c
-- ON rc.CuisineID = c.CuisineID
-- WHERE c.CuisineName = 'Pizza'
-- AND r.Rating > 4;

-- Problem 2 -- Deliverables:
-- Find all restaurants in the same city that serve at least one cuisine in common. Show the following details for each pair of restaurants:
-- Restaurant 1 Name
-- Restaurant 2 Name
-- Shared Cuisine
-- City

-- CREATE TABLE restaurants (
--     RestaurantID INT PRIMARY KEY,
--     RestaurantName VARCHAR(255),
--     CountryCode CHAR(2),
--     City VARCHAR(100),
--     Address VARCHAR(255),
--     Locality VARCHAR(255),
--     LocalityVerbose VARCHAR(255),
--     Currency VARCHAR(10),
--     Price_range INT,
--     Average_Cost_for_two INT,
--     Votes INT,
--     Rating FLOAT
-- );

-- CREATE TABLE restaurant_features (
--     RestaurantID INT,
--     Has_Table_booking BOOLEAN,
--     Has_Online_delivery BOOLEAN,
--     Is_delivering_now BOOLEAN,
--     Switch_to_order_menu BOOLEAN,
--     FOREIGN KEY (RestaurantID) REFERENCES restaurants(RestaurantID)
-- );

-- CREATE TABLE cuisines (
--     CuisineID INT PRIMARY KEY,
--     CuisineName VARCHAR(255)
-- );

-- CREATE TABLE restaurant_cuisines (
--     RestaurantID INT,
--     CuisineID INT,
--     FOREIGN KEY (RestaurantID) REFERENCES restaurants(RestaurantID),
--     FOREIGN KEY (CuisineID) REFERENCES cuisines(CuisineID)
-- );


-- Write your code here
-- SELECT 
-- r1.RestaurantName AS RestaurantName1, 
-- r2.RestaurantName AS RestaurantName2, 
-- c.CuisineName, r1.City
-- FROM restaurants r1
-- JOIN restaurants r2
-- ON r1.city = r2.city
--     AND r1.RestaurantID < r2.RestaurantID
-- JOIN restaurant_cuisines rc1
--     ON r1.RestaurantID = rc1.RestaurantID
-- JOIN restaurant_cuisines rc2
--     ON r2.RestaurantID = rc2.RestaurantID
--     AND rc1.CuisineID = rc2.CuisineID
-- JOIN cuisines c
-- ON rc1.CuisineID = c.CuisineID;

-- Problem3 :
-- Deliverables:
-- List all restaurants along with the cuisines they serve. 
-- This query should ensure that all restaurants are included in the result, 
-- regardless of whether they are associated with any cuisine.
-- Hint: Use a LEFT JOIN to combine the Restaurant table, 
-- the Restaurant_Cuisines junction table, and the Cuisine table. 
-- This will allow us to capture restaurants without any assigned cuisines and highlight them in the output.

-- CREATE TABLE restaurants (
--     RestaurantID INT PRIMARY KEY,
--     RestaurantName VARCHAR(255),
--     CountryCode CHAR(2),
--     City VARCHAR(100),
--     Address VARCHAR(255),
--     Locality VARCHAR(255),
--     LocalityVerbose VARCHAR(255),
--     Currency VARCHAR(10),
--     Price_range INT,
--     Average_Cost_for_two INT,
--     Votes INT,
--     Rating FLOAT
-- );

-- CREATE TABLE restaurant_features (
--     RestaurantID INT,
--     Has_Table_booking BOOLEAN,
--     Has_Online_delivery BOOLEAN,
--     Is_delivering_now BOOLEAN,
--     Switch_to_order_menu BOOLEAN,
--     FOREIGN KEY (RestaurantID) REFERENCES restaurants(RestaurantID)
-- );

-- CREATE TABLE cuisines (
--     CuisineID INT PRIMARY KEY,
--     CuisineName VARCHAR(255)
-- );

-- CREATE TABLE restaurant_cuisines (
--     RestaurantID INT,
--     CuisineID INT,
--     FOREIGN KEY (RestaurantID) REFERENCES restaurants(RestaurantID),
--     FOREIGN KEY (CuisineID) REFERENCES cuisines(CuisineID)
-- );
-- INSERT INTO Restaurants 
-- (RestaurantID, RestaurantName, CountryCode, City, Address, Locality, LocalityVerbose, Currency, Price_range, Average_Cost_for_two, Votes, Rating)
-- VALUES
-- (3400019, 'Dasaprakash Restaurant', 'IN', 'Agra', 'Meher Cinema Complex, Gwalior Road, Rakabganj, Agra', 'Rakabganj', 'Rakabganj, Agra', 'Indian Rupees(Rs.)', 2, 550, 121, 4.1),

-- (3400033, 'The Charcoal Chimney', 'IN', 'Agra', 'Hotel Samovar, Fatehabad Road, Tajganj, Agra', 'Tajganj', 'Tajganj, Agra', 'Indian Rupees(Rs.)', 3, 1100, 70, 3.4),

-- (3400346, 'Sheroes Hangout', 'IN', 'Agra', 'Opposite The Gateway Hotel, Fatehabad Road, Tajganj, Agra', 'Tajganj', 'Tajganj, Agra', 'Indian Rupees(Rs.)', 1, 0, 77, 4.9),

-- (3400350, 'Bon Barbecue', 'IN', 'Agra', 'Parador Hotel, 3A-3B, Phase 1, Fatehabad Road, Taj Nagri, Tajganj, Agra', 'Tajganj', 'Tajganj, Agra', 'Indian Rupees(Rs.)', 4, 1500, 57, 3.8),

-- (3400391, 'Chapter 1 Cafe', 'IN', 'Agra', '1374 K/1375 K, 2nd floor, Dinesh Nagar, Fatehbad Road, Tajganj, Agra', 'Tajganj', 'Tajganj, Agra', 'Indian Rupees(Rs.)', 1, 0, 98, 3.9),

-- (3400016, 'Pind Balluchi', 'IN', 'Agra', 'Opposite Saga Emporium, Fatehabad Road, Tajganj, Agra', 'Tajganj', 'Tajganj, Agra', 'Indian Rupees(Rs.)', 3, 900, 175, 3.7);
-- INSERT INTO restaurant_features
-- (RestaurantID, Has_Table_booking, Has_Online_delivery, Is_delivering_now, Switch_to_order_menu)
-- VALUES
-- (3400019, FALSE, FALSE, FALSE, FALSE),
-- (3400033, FALSE, FALSE, FALSE, FALSE),
-- (3400346, FALSE, FALSE, FALSE, FALSE),
-- (3400350, FALSE, FALSE, FALSE, FALSE),
-- (3400391, FALSE, FALSE, FALSE, FALSE),
-- (3400016, FALSE, FALSE, FALSE, FALSE);

-- INSERT INTO cuisines (CuisineID, CuisineName)
-- VALUES
-- (1, 'South Indian'),
-- (2, 'Chinese'),
-- (3, 'North Indian'),
-- (4, 'Desserts'),
-- (5, 'Cafe'),
-- (6, 'Continental'),
-- (7, 'Mughlai'),
-- (8, 'Italian'),
-- (9, 'Mexican'),
-- (10, 'Rajasthani');
-- INSERT INTO restaurant_cuisines (RestaurantID, CuisineID)
-- VALUES
-- (3400019, 1),
-- (3400019, 4),

-- (3400033, 3),
-- (3400033, 2),

-- (3400346, 5),
-- (3400346, 3),

-- (3400350, 3),
-- (3400350, 2),

-- (3400391, 5),
-- (3400391, 6),
-- (3400391, 3),
-- (3400391, 8),

-- (3400016, 3),
-- (3400016, 7);
-- ALTER TABLE Restaurants
-- MODIFY Currency VARCHAR(30);
-- DESCRIBE Restaurants; --DESCRIBE is use to Check Column Size;

-- Write your code here
-- SELECT r.RestaurantName, c.CuisineName AS Cuisine
-- FROM restaurants r
-- LEFT JOIN restaurant_cuisines rc
-- ON r.RestaurantID = rc.RestaurantID
-- LEFT JOIN cuisines c
-- ON rc.CuisineID = c.CuisineID;
-- CREATE DATABASE employee_db;
-- CREATE DATABASE orders_db;
-- CREATE TABLE employee_db(
-- emp_id INT PRIMARY KEY,
-- name VARCHAR(50),
-- department VARCHAR(50),
-- salary INT,
-- manager_id INT
-- );
-- CREATE TABLE orders_db(
-- order_id INT PRIMARY KEY,
-- emp_id INT,
-- amount INT,
-- order_date DATE,
-- FOREIGN KEY(emp_id) REFERENCES employee_db(emp_id)
-- )


-- INSERT INTO employee_db (emp_id, name, department, salary, manager_id) VALUES
-- (1, 'Asha', 'HR', 40000, NULL),
-- (2, 'Ravi', 'IT', 60000, 5),
-- (3, 'Neha', 'IT', 75000, 5),
-- (4, 'Arjun', 'Sales', 50000, 6),
-- (5, 'Kiran', 'IT', 90000, NULL),
-- (6, 'Meera', 'Sales', 80000, NULL),
-- (7, 'Tara', 'HR', 42000, 1);
-- INSERT INTO employee_db(emp_id, name, department, salary, manager_id) VALUES 
-- (8, 'Ram', 'IT', 80000, 2);

-- INSERT INTO orders_db (order_id, emp_id, amount, order_date) VALUES
-- (101, 2, 5000, '2024-01-10'),
-- (102, 3, 7000, '2024-01-15'),
-- (103, 2, 3000, '2024-02-01'),
-- (104, 4, 4000, '2024-02-10'),
-- (105, 3, 2000, '2024-03-05');

-- * Que 1 DUPLICATE SALARY *
-- SELECT salary, COUNT(*)
-- FROM employee_db
-- GROUP BY salary
-- HAVING COUNT(*) > 1;

-- * Que2 Total order amount per employee *
-- SELECT e.name, SUM(o.amount) AS total_amount
-- FROM employee_db e
-- LEFT JOIN orders_db o
-- ON e.emp_id = o.emp_id
-- GROUP BY e.name;


-- * Que3 Second highest salary
-- SELECT Max(salary)
-- FROM employee_db
-- WHERE salary < (SELECT MAX(salary) FROM employee_db);

-- (SELECT MAX(salary) FROM employee_db) ye kya degi 
-- Output 90000
-- then humne bola hai outer query me select karo max salary jo ki choti ho max salary se
-- SELECT Max(salary)
-- FROM employee_db
-- WHERE salary ye output 80000 dega ar comparison aisa ayega (WHERE salary < 90000) 80000 < 90000
-- Output me 80000 dedega;

-- Que3 Find employees earning more than their manager.
-- SELECT e.name, e.salary
-- FROM employee_db e
-- JOIN employee_db m
-- ON e.manager_id = m.emp_id 
-- WHERE e.salary > m.salary;
-- SELECT * FROM employee_db;

-- Que4 Find average salary of employees?
-- SELECT AVG(salary) FROM employee_db;

-- Que5 Find departments having more than 1 employee?
-- SELECT department, COUNT(*) AS total_employee
-- FROM employee_db
-- GROUP BY department
-- HAVING COUNT(*) > 1;

-- Q6: Find total employees in each department.
SELECT department, COUNT(*) AS total
FROM employee_db
GROUP BY department;


-- Use Of DISTINCT
-- SELECT DISTINCT salary
-- FROM employee_db
-- ORDER BY salary DESC
-- LIMIT 1 OFFSET 1;


	