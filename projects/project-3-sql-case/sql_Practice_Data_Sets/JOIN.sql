-- CREATE DATABASE hotelReservationSystem;
-- USE hotelReservationSystem;
-- Create Table Customers ( 
-- 	CustomerID INT AUTO_INCREMENT PRIMARY KEY, 
-- 	CustomerName VARCHAR(50)
-- );
-- INSERT INTO Customers (CustomerName) VALUES('John'),('Sarah'),('David');
-- CREATE TABLE Orders (
--     OrderID INT PRIMARY KEY,
--     CustomerID INT,
--     OrderDate DATE
-- );
-- INSERT INTO Orders VALUES
-- (101,1,'2024-01-01'),
-- (102,2,'2024-01-02'),
-- (103,4,'2024-01-03');  -- Customer 4 does not exist
-- SELECT Customers.CustomerID, CustomerName, OrderID
-- FROM Customers
-- LEFT JOIN Orders
-- ON Customers.CustomerID = Orders.CustomerID;
SELECT Customers.CustomerID, CustomerName, OrderID
FROM Customers
RIGHT JOIN Orders
ON Customers.CustomerID = Orders.CustomerID;