USE ecom;
-- 01 Task : Write an SQL query to find the names of customers who do not have a referee with  id= 2. Return the result table in any order.
-- CREATE TABLE IndCustomer (
--     id INT PRIMARY KEY,
--     name VARCHAR(50),
--     referee_id INT
-- );

-- INSERT INTO IndCustomer (id, name, referee_id) VALUES
-- (1, 'Will', NULL),
-- (2, 'Jane', NULL),
-- (3, 'Alex', 2),
-- (4, 'Bill', NULL),
-- (5, 'Zack', 1),
-- (6, 'Mark', 2);

-- SELECT name FROM IndCustomer
-- WHERE referee_id != 2 OR referee_id IS NULL;

-- CREATE TABLE World (
--     name VARCHAR(50),
--     continent VARCHAR(50),
--     area INT,
--     population INT,
--     gdp BIGINT
-- );

-- 02 Task :
-- A country is considered big if:
-- It has an area of at least 3,000,000 km², or
-- It has a population of at least 25,000,000 people.
-- Write an SQL query to find the name, population, and area of the big countries.

-- INSERT INTO World (name, continent, area, population, gdp) VALUES
-- ('USA', 'North America', 9833517, 331000000, 21000000000),
-- ('Canada', 'North America', 9984670, 38000000, 1800000000),
-- ('Iceland', 'Europe', 103000, 370000, 24000000),
-- ('Brazil', 'South America', 8515767, 212000000, 2200000000);

-- SELECT name, population, area FROM World
-- WHERE area >=3000000 OR population >= 2500000;


-- 03 Task: Find all author_id whose articles were viewed by themselves (author_id = viewer_id).
-- Return results in ascending order of author_id.

-- CREATE TABLE Views (
--     article_id INT,
--     author_id INT,
--     viewer_id INT,
--     view_date DATE
-- );

-- INSERT INTO Views (article_id, author_id, viewer_id, view_date) VALUES
-- (1, 3, 5, '2019-08-01'),
-- (1, 3, 3, '2019-08-02'),
-- (2, 7, 7, '2019-08-01'),
-- (3, 4, 8, '2019-08-01');

-- SELECT author_id AS id FROM Views 
-- WHERE author_id = viewer_id;

-- 04 Task : Write an SQL query to find the IDs of all invalid tweets.
-- Return the result table in any order. 
-- A tweet is considered invalid if the number of characters in the content is strictly greater than 15.

-- CREATE TABLE Tweets (
--     tweet_id INT PRIMARY KEY,
--     content VARCHAR(255)
-- );

-- INSERT INTO Tweets (tweet_id, content) VALUES
-- (1, 'Vote for Biden'),
-- (2, 'Let us make America great again!'),
-- (3, 'Covid19 is scary'),
-- (4, 'Stay safe!'),
-- (5, 'Time for change');
-- SELECT * FROM Tweets;

-- SELECT tweet_id FROM Tweets 
-- WHERE LENGTH(content) > 15; 

-- Problem : 05 Task
-- Write an SQL query that reports the product_name, year, 
-- and price for each sale in the Sales table.

-- CREATE TABLE Sales (
--     sale_id INT,
--     product_id INT,
--     year INT,
--     quantity INT,
--     price INT
-- );

-- CREATE TABLE Product (
--     product_id INT,
--     product_name VARCHAR(255)
-- );

-- INSERT INTO Sales (sale_id, product_id, year, quantity, price) VALUES
-- (1, 100, 2008, 10, 5000),
-- (2, 100, 2009, 12, 5000),
-- (7, 200, 2011, 15, 9000);

-- INSERT INTO Product (product_id, product_name) VALUES
-- (100, 'Nokia'),
-- (200, 'Apple'),
-- (300, 'Samsung');
-- SELECT Product.product_name, Sales.quantity
-- FROM Sales
-- INNER JOIN Product
-- ON Sales.product_id = Product.product_id;


-- CREATE TABLE Visits (
--     visit_id INT PRIMARY KEY,
--     customer_id INT
-- );

-- CREATE TABLE Transactions (
--     transaction_id INT PRIMARY KEY,
--     visit_id INT,
--     amount INT
-- );

-- INSERT INTO Visits (visit_id, customer_id) VALUES
-- (1, 23),
-- (2, 9),
-- (4, 30),
-- (5, 54),
-- (6, 96);

-- INSERT INTO Transactions (transaction_id, visit_id, amount) VALUES
-- (2, 5, 310),
-- (3, 5, 300),
-- (9, 1, 200),
-- (12, 6, 910);

-- Task 06: Write an SQL query to find the IDs of the customers who 
-- visited the mall but did not make any transactions. Return the result table in any order.
-- SELECT V.customer_id FROM Visits V
-- LEFT JOIN Transactions T
-- ON V.visit_id = T.visit_id
-- WHERE T.transaction_id IS NULL;

-- 07 Problem:
-- Write an SQL query to find the number of unique subjects each teacher teaches.
-- Return the result table with columns: teacher_id,
-- cnt (the number of unique subjects taught by that teacher).

-- CREATE TABLE Teacher (
--     teacher_id INT,
--     subject_id INT,
--     dept_id INT
-- );

-- INSERT INTO Teacher (teacher_id, subject_id, dept_id) VALUES
-- (1, 2, 3),
-- (1, 2, 4),
-- (1, 3, 3),
-- (2, 1, 1),
-- (2, 2, 1),
-- (3, 4, 2);

-- SELECT teacher_id, 
-- COUNT(DISTINCT subject_id) As cnt 
-- FROM Teacher 
-- GROUP BY teacher_id;

-- Task 08: Write an SQL query to find the average time each machine takes to complete a process.
-- A process starts with an entry having activity_type = 'start' and ends with activity_type = 'end'.
-- The time to complete a process is the end.timestamp - start.timestamp.
-- Round the result to 3 decimal places.

-- CREATE TABLE Activity (
--     machine_id INT,
--     process_id INT,
--     activity_type VARCHAR(10),
--     timestamp FLOAT
-- );

-- INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES
-- (1, 1, 'start', 0.712),
-- (1, 1, 'end', 1.520),
-- (2, 1, 'start', 0.115),
-- (2, 1, 'end', 0.620),
-- (2, 2, 'start', 0.400),
-- (2, 2, 'end', 1.200);

-- SELECT a.machine_id, 
--     ROUND(AVG(b.timestamp-a.timestamp),3) AS processing_time
-- FROM Activity a
-- JOIN Activity b
-- ON a.machine_id = b.machine_id
-- AND a.activity_type = 'start'
-- AND b.activity_type = 'end'
-- AND a.process_id = b.process_id
-- GROUP BY a.machine_id;

-- Task 09 : Count how many exams each student wrote (ignore subjects they never wrote).
-- CREATE TABLE Students (
-- student_id INT,
-- student_name VARCHAR(50)
-- );

-- CREATE TABLE Examinations (
-- student_id INT,
-- subject_id INT
-- );

-- INSERT INTO Students (student_id, student_name) VALUES
-- (1, 'Alice'),
-- (2, 'Bob');

-- INSERT INTO Examinations (student_id, subject_id) VALUES
-- (1, 101),
-- (1, 101),
-- (2, 102);
-- SELECT S.student_id, S.student_name, 
-- COUNT(E.subject_id) AS exams_count 
-- FROM Students S
-- LEFT JOIN Examinations E
-- ON S.student_id = E.student_id
-- GROUP BY S.student_id, S.student_name ;

-- Task 10: Write an SQL query to report the name and bonus amount of each employee who received less than 1000 bonus or no bonus at all.
-- Return the result table ordered by empId.

-- CREATE TABLE Employee (
--     empId INT PRIMARY KEY,
--     name VARCHAR(50),
--     supervisor INT,
--     salary INT
-- );

-- CREATE TABLE Bonus (
-- 	empId INT,
-- 	bonus INT
--  );

-- INSERT INTO Employee (empId, name, supervisor, salary) VALUES
-- (1, 'Alice', 3, 6000),
-- (2, 'Bob', 1, 5000),
-- (3, 'Charlie', NULL, 7000);

-- INSERT INTO Bonus (empId, bonus) VALUES
-- (1, 500),
-- (2, 1500);

-- SELECT Employee.name, Bonus.bonus 
-- FROM Employee
-- LEFT JOIN Bonus
-- ON Employee.empId = Bonus.empId
-- WHERE  Bonus<1000 OR Bonus IS NULL
-- ORDER BY Employee.empId;

-- Task 10: Write an SQL query to find the average selling price for each product.
-- Average Selling Price = ∑(price×units)/∑(units)
-- Round the result to 2 decimal places.The result should return (product_id, average_price).

-- CREATE TABLE ProductPrices (
--     product_id INT,
--     start_date DATE,
--     end_date DATE,
--     price INT
-- );

-- CREATE TABLE UnitsSold (
--     product_id INT,
--     purchase_date DATE,
--     units INT
-- );

-- INSERT INTO ProductPrices VALUES
-- (1, '2019-02-17', '2019-02-28', 5),
-- (1, '2019-03-01', '2019-03-22', 20),
-- (2, '2019-02-01', '2019-02-20', 15);

-- INSERT INTO UnitsSold VALUES
-- (1, '2019-02-25', 100),
-- (1, '2019-03-01', 15),
-- (2, '2019-02-10', 200),
-- (2, '2019-03-22', 30);

-- SELECT P.product_id,
--     ROUND(SUM(P.price * U.units)*1.0/SUM(U.units), 2) 
--     AS average_price
-- FROM Prices P 
-- JOIN UnitsSold U
-- ON P.product_id = U.product_id
-- AND U.purchase_date BETWEEN p.start_date AND p.end_date  
-- GROUP BY p.product_id;

-- Task 11: Count Users Registered per Contest
-- You are given table Register containing contest registrations.
-- Return how many users participated in each contest.
-- CREATE TABLE Register (
-- contest_id INT,
-- user_id INT
-- );

-- INSERT INTO Register (contest_id, user_id) VALUES
-- (101, 1),
-- (101, 2),
-- (102, 2);

-- SELECT contest_id, COUNT(user_id) AS total_users
-- FROM Register
-- GROUP BY contest_id;

-- Problem 12: For each customer, check if their first order (earliest date) was delivered on their preferred date, and return Yes/No.

-- CREATE TABLE Delivery (
-- order_id INT,
-- customer_id INT,
-- order_date DATE,
-- customer_pref_delivery_date DATE
-- );

-- INSERT INTO Delivery (order_id, customer_id, order_date, customer_pref_delivery_date) VALUES
-- (1, 1, '2025-01-01', '2025-01-01'),
-- (2, 1, '2025-01-02', '2025-01-03');
-- SELECT * FROM Delivery;

-- SELECT customer_id,
-- 	CASE
-- 		WHEN order_date = customer_pref_delivery_date THEN 'YES'
-- 		ELSE 'No'
-- 	END AS deleivered_on_time
-- FROM Delivery
-- WHERE (customer_id, order_date) IN (
-- SELECT customer_id, MIN(order_date)
-- FROM Delivery
-- GROUP BY customer_id
-- );
-- * For above the same solution using JOIN *
-- and also explain why many SQL engineers prefer it over IN.

-- SELECT d.customer_id,
--        CASE 
--            WHEN d.order_date = d.customer_pref_delivery_date THEN 'YES'
--            ELSE 'No'
--        END AS delivered_on_time
-- FROM Delivery d
-- JOIN (
--         SELECT customer_id, MIN(order_date) AS first_order
--         FROM Delivery
--         GROUP BY customer_id
--      ) f
-- ON d.customer_id = f.customer_id
-- AND d.order_date = f.first_order;
-- Same Question solve by Query Using ROW_NUMBER()
-- SELECT customer_id,
--        CASE
--            WHEN order_date = customer_pref_delivery_date THEN 'YES'
--            ELSE 'No'
--        END AS delivered_on_time
-- FROM (
--         SELECT *,
--                ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn
--         FROM Delivery
--      ) t
-- WHERE rn = 1;

-- Problem 13 : Return each employee with their category:
-- CREATE TABLE CategorizeEmployee (
-- id INT,
-- name VARCHAR(50),
-- salary INT
-- );

-- INSERT INTO CategorizeEmployee (id, name, salary) VALUES
-- (1, 'Alice', 3500),
-- (2, 'Bob', 5000),
-- (3, 'Charlie', 8000);

-- DELETE FROM CategorizeEmployee
-- WHERE id IN (
--     SELECT id
--     FROM (
--         SELECT id,
--                ROW_NUMBER() OVER(PARTITION BY id, name, salary ORDER BY id) AS rn
--         FROM CategorizeEmployee
--     ) t
--     WHERE rn > 1
-- );
-- SELECT * FROM CategorizeEmployee;

-- SELECT id,
-- 	CASE 
-- 		WHEN salary<4000 THEN 'Low'
-- 		WHEN salary BETWEEN 4000 AND 7000 THEN 'Medium'
--         ELSE 'High'
-- 	END AS category
-- FROM CategorizeEmployee;

-- Problem 14: Write an SQL query to find, for each user, the percentage of queries that have a score >= 60.
-- Round the percentage to 2 decimal places.
-- Return columns (user_id, user_name, quality_percentage)
-- Sort by user_id ASC.
-- * Queries Quality and Percentage * 

-- CREATE TABLE QualityUsers (
--     user_id INT PRIMARY KEY,
--     user_name VARCHAR(50)
-- );

-- CREATE TABLE Queries (
--     query_id INT PRIMARY KEY,
--     user_id INT,
--     score INT
-- );

-- INSERT INTO QualityUsers VALUES
-- (1, 'Alice'),
-- (2, 'Bob'),
-- (3, 'Charlie');

-- INSERT INTO Queries VALUES
-- (101, 1, 70),
-- (102, 1, 50),
-- (103, 2, 80),
-- (104, 3, 40);
-- SELECT score >= 60 AS quality_percentage

-- SELECT 
-- 	U.user_id, 
-- 	U.user_name, 
-- 	ROUND(
--     SUM(CASE 
-- 			WHEN Q.score >=60 THEN 1
--             ELSE 0 
--             END)/ COUNT(Q.query_id) * 100, 2) 
--             AS quality_percentage
-- FROM QualityUsers U
-- LEFT JOIN Queries Q
-- ON U.user_id = Q.user_id
-- GROUP BY U.user_id, U.user_name
-- ORDER BY U.user_id;


-- SELECT U.user_id, U.user_name,
-- ROUND(
--     SUM(
--     CASE 
--         WHEN Q.score >= 60 THEN 1
--         ELSE 0
--         END) * 100.0/ NULLIF (COUNT (Q.query_id), 0),
--         2)
--     AS quality_percentage
-- FROM Users U
-- LEFT JOIN Queries Q
-- ON U.user_id = Q.user_id
-- GROUP BY U.user_id, U.user_name
-- ORDER BY U.user_id;

-- Problem: Write an SQL query to find the number of times each student attended each exam for every subject.
-- CREATE TABLE Students1 (
--     student_id INT,
--     student_name VARCHAR(50)
-- );

-- CREATE TABLE Subjects (
--     subject_id INT,
--     subject_name VARCHAR(50)
-- );

-- CREATE TABLE Examinations (
--     student_id INT,
--     subject_id INT
-- );

-- INSERT INTO Students1 VALUES (1, 'Alice'), (2, 'Bob');
-- INSERT INTO Subjects VALUES (101, 'Math'), (102, 'Physics');
-- INSERT INTO Examinations VALUES (1, 101), (1, 101), (2, 102);


-- SELECT 
-- S.student_id, 
-- S.student_name,
-- Sub.subject_id,
-- Sub.subject_name,
-- COUNT(E.subject_id) AS attended_exams
-- FROM Students1 S
-- CROSS JOIN Subjects Sub
-- LEFT JOIN Examinations E
-- ON S.student_id = E.student_id
-- AND Sub.subject_id = E.subject_id
-- GROUP BY S.student_id, S.student_name, Sub.subject_id, Sub.subject_name
-- ORDER BY student_id, subject_id;



-- Problem :-
-- Write an SQL query to find managers who have at least 5 direct reports.
-- Return the result with the following columns:
-- name — manager name
-- CREATE TABLE DirectReporties (
--     id INT,
--     name VARCHAR(50),
--     department VARCHAR(50),
--     managerId INT
-- );

-- Example inserts
-- INSERT INTO DirectReporties VALUES
-- (1, 'John', 'HR', NULL),
-- (2, 'Dan', 'IT', 1),
-- (3, 'James', 'IT', 1),
-- (4, 'Amy', 'IT', 1),
-- (5, 'Anne', 'IT', 1),
-- (6, 'Ron', 'IT', 1);

-- SELECT name
-- FROM DirectReporties
-- WHERE id IN(
-- 	SELECT managerId
--     FROM DirectReporties 
--     GROUP BY managerId
--     HAVING COUNT(*) >= 5
-- );

-- SELECT m.name
-- FROM DirectReporties m
-- JOIN DirectReporties E
-- ON m.id = E.managerId
-- GROUP BY m.id, m.name
-- HAVING COUNT(E.id) >=5;

-- Problem :
-- What to Find:
-- For each contest_id, return the percentage of users registered out of total users.
-- Round the percentage to two decimal places.
-- Return contest_id and percentage.
-- Sort by percentage DESC, then by contest_id ASC.

-- CREATE TABLE PercentageOfUsers (
--     user_id INT PRIMARY KEY,
--     user_name VARCHAR(50)
-- );

-- CREATE TABLE Register (
--     contest_id INT,
--     user_id INT,
--     PRIMARY KEY (contest_id, user_id)
-- );

-- INSERT INTO PercentageOfUsers VALUES
-- (1, 'Alice'),
-- (2, 'Bob'),
-- (3, 'Charlie');

-- INSERT INTO Register VALUES
-- (101, 1),
-- (101, 2),
-- (102, 2);

-- SELECT R.contest_id,
-- 	ROUND(COUNT(R.user_id) * 100 /
--     (SELECT COUNT(*) FROM PercentageOfUsers), 2) AS Percentage
-- FROM Register R
-- GROUP By R.contest_id
-- ORDER BY percentage DESC ;

-- Problem : Write an SQL query to find, for each customer, the percentage of orders delivered on the customer’s preferred delivery date.
-- Only consider the earliest order per customer (first order).
-- Return columns (customer_id, immediate_percentage).
-- Round the percentage to 2 decimal places.
-- Sort by customer_id ASC.

-- CREATE TABLE ImmediateFoodDelivery (
--     order_id INT,
--     customer_id INT,
--     order_date DATE,
--     customer_pref_delivery_date DATE
-- );

-- INSERT INTO ImmediateFoodDelivery VALUES
-- (1, 1, '2025-01-01', '2025-01-01'),
-- (2, 1, '2025-01-02', '2025-01-03'),
-- (3, 2, '2025-01-01', '2025-01-01'),
-- (4, 2, '2025-01-03', '2025-01-03');

-- SELECT customer_id,
--     ROUND(
--      AVG(
--         CASE 
--             WHEN order_date = customer_pref_delivery_date 
--             THEN 1
--             ELSE 0
--         END 
--         ) * 100.0, 2) AS immediate_percentage
-- FROM ImmediateFoodDelivery
-- WHERE(customer_id, order_date) IN (
--     SELECT customer_id, MIN(order_date) 
--     FROM ImmediateFoodDelivery
--     GROUP BY customer_id
-- )
-- GROUP BY customer_id
-- ORDER BY customer_id ASC;

-- Write an SQL query to find the classes that have at least 5 students.
-- Return a single column: class
-- Sort the result by class in ascending order.

-- CREATE TABLE Classes (
--     student_id INT,
--     class VARCHAR(50)
-- );

-- INSERT INTO Classes VALUES
-- (1, 'Math'),
-- (2, 'Math'),
-- (3, 'Math'),
-- (4, 'Math'),
-- (5, 'Math'),
-- (6, 'Physics'),
-- (7, 'Physics');

-- SELECT class
-- FROM Classes
-- GROUP BY class
-- HAVING COUNT(*) >=5
-- ORDER BY class ASC;


-- CREATE TABLE SalesAnalysis (
--     product_id INT,
--     store_id INT,
--     quantity INT,
--     price INT
-- );

-- INSERT INTO SalesAnalysis VALUES
-- (1, 1, 100, 20),
-- (1, 2, 50, 30),
-- (2, 1, 200, 15),
-- (2, 2, 100, 15);

-- SELECT product_id, store_id, MAX(price)
-- FROM SalesAnalysis
-- GROUP BY product_id
-- ORDER BY product_id, store_id ASC;

-- * BY JOIN *
-- SELECT s.product_id, s.store_id, s.price
-- FROM Sales s
-- JOIN
-- (
--     SELECT product_id, MAX(price) AS max_price
--     FROM Sales
--     GROUP BY product_id
-- ) m
-- ON s.product_id = m.product_id
-- AND s.price = m.max_price
-- ORDER BY s.product_id, s.store_id;


-- SELECT s.*
-- FROM Sales s
-- JOIN (
--     SELECT product_id, MAX(price) max_price
--     FROM Sales
--     GROUP BY product_id
-- ) m
-- ON s.product_id = m.product_id
-- AND s.price = m.max_price;

-- * BY WINDOW FUNCTION *
-- SELECT product_id, store_id, price
-- FROM ( 
--     SELECT *, 
--     RANK() OVER(PARTITION BY product_id ORDER BY price DESC) AS r
--     FROM Sales) t
-- WHERE r=1
-- ORDER BY product_id, store_id;

-- Write an SQL query to find the number of followers for each user.
-- Return columns: (user_id, follower_count)
-- Include users who have zero followers.
-- Sort the result by user_id ASC.     

-- CREATE TABLE Followers (
--     user_id INT,
--     follower_id INT
-- );

-- INSERT INTO Followers VALUES
-- (1, 2),
-- (1, 3),
-- (2, 1),
-- (3, 1);

-- SELECT * FROM Followers;

SELECT u.user_id,
       COUNT(f.follower_id) AS follower_count
FROM (
      SELECT DISTINCT user_id FROM Followers
      UNION
      SELECT DISTINCT follower_id FROM Followers
     ) AS u
LEFT JOIN Followers f
ON u.user_id = f.user_id
GROUP BY u.user_id
ORDER BY u.user_id;

-- SELECT user_id,
-- COUNT(follower_id) AS follower_count
-- FROM Followers
-- GROUP BY user_id
-- ORDER BY user_id ASC;

-- Problem
-- Write an SQL query to count the number of employees in each salary category according to the following rules:
-- "Low": salary < 4000
-- "Medium": 4000 <= salary <= 7000
-- "High": salary > 7000
-- Return the result with columns: (category, employee_count)
-- Sort by category in ascending order (High, Low, Medium).
-- Hint: Make use of UNION ALL 

-- CREATE TABLE Employee_UNION_ALL (
--     id INT,
--     name VARCHAR(50),
--     salary INT
-- );

-- INSERT INTO Employee_UNION_ALL VALUES
-- (1, 'Alice', 3500),
-- (2, 'Bob', 5000),
-- (3, 'Charlie', 8000);

-- SELECT (
-- SELECT 'Low' AS category, COUNT(*) AS employee_count
-- FROM Employee_UNION_ALL
-- Where salary < 4000

-- UNION ALL

-- SELECT 'Medium' AS category, COUNT(*)
-- FROM Employee_UNION_ALL 
-- WHERE salary BETWEEN 4000 AND 7000

-- UNION ALL 

-- SELECT 'High' AS category, COUNT(*) 
-- FROM Employee_UNION_ALL
-- WHERE salary > 7000

-- ORDER BY category;