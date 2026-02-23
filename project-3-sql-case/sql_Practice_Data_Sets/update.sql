USE ecom;
-- #Products Table Using UPDATE

-- CREATE TABLE Products (
--     product_id INT,
--     product_name VARCHAR(255),
--     category VARCHAR(255),
--     price INT,
--     in_stock VARCHAR(3)
-- );

-- INSERT INTO Products (product_id, product_name, category, price, in_stock)
-- VALUES
-- (1, 'Smartphone', 'Electronics', 50000, 'Yes'),
-- (2, 'Microwave Oven', 'Appliances', 15000, 'No'),
-- (3, 'Laptop', 'Electronics', 70000, 'Yes'),
-- (4, 'Vacuum Cleaner', 'Appliances', 12000, 'Yes'),
-- (5, 'Wireless Earbuds', 'Electronics', 3000, 'Yes');

-- Write your code here
-- Q Write a query to retrieve all products that:
-- 1. Belong to the Electronics category AND cost more than 10,000.
-- 2. OR are in stock in the Appliances category.

-- SELECT * FROM Products 
-- WHERE 
-- (category="Electronics" AND price>10000) 
-- OR 
-- (category="Appliances" AND in_stock="Yes");

-- #ORDER Table Using UPDATE

-- UPDATE orders
-- SET order_status = 'Delivered'
-- WHERE order_id = 10;

UPDATE orders 
SET discount_percent = 10, rating = 4
WHERE customer_name = "Neha Verma";

