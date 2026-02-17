USE ecom;
-- SELECT * FROM orders;
-- CREATE TABLE customers(
-- customer_id INT PRIMARY KEY AUTO_INCREMENT,
-- name VARCHAR(100),
-- email VARCHAR(150),
-- age INT,
-- phone VARCHAR(15),
-- is_active BOOLEAN,
-- signup_date DATE,
-- created_at DATETIME,
-- total_spent DECIMAL(10,2)
-- );

-- DROP TABLE customers;
-- delete the table from the database

-- ALTER TABLE customers RENAME TO client;
-- It changes table name: users  ➝  customers
-- The table structure and data stay same.Only the name changes.
-- RENAME TABLE users TO customers;
-- customers ➝ users Table name becomes users again Basically rename → then rename back.
-- RENAME TABLE customers TO users;

-- INSERT INTO customers(name, email, age, phone, is_active, signup_date, created_at, total_spent)
-- VALUES ('Amit Sharma', 'amit@gmail.com', 28, '8908937837', TRUE, '2025-01-10', '2025-01-10 10:30:00', 1266.56);

-- INSERT INTO customers
-- (name, email, age, phone, is_active, signup_date, created_at, total_spent)
-- VALUES
-- ('Neha Verma', 'neha@gmail.com', 25, '9123456789', TRUE, '2025-01-12', '2025-01-12 09:15:00', 5400.00),
-- ('Rahul Khan', 'rahul@gmail.com', 32, '9988776655', FALSE, '2025-01-15', '2025-01-15 14:20:00', 0.00);
SELECT * FROM customers;

-- DELETE FROM customers WHERE customer_id > 3;

-- SELECT * FROM customers 
-- WHERE customer_id NOT IN (
-- SELECT MIN(customer_id)FROM customers GROUP BY email);
-- ALTER TABLE customers ADD CONSTRAINT unique_email UNIQUE (email); 
