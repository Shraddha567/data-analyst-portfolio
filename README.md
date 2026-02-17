# Data Analyst Portfolio – by Shraddha Maheshwari

SQL Case Study (25+ queries)

CRUD Operations
CRUD stands for Create, Read, Update, Delete. These are the four basic operations we can perform on data in a database.

Create: Adding new data (using INSERT).
Read: Retrieving data (using SELECT).
Update: Modifying existing data (using UPDATE).
Delete: Removing data (using DELETE).

Resetting the Database
DROP DATABASE IF EXISTS ecom;

Deletes the database if it already exists so we can start fresh.

Creating and Using the Database
CREATE DATABASE ecom;
USE ecom;

Creates a new database named ecom and sets it as the active database.

Creating the orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    product VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    price_per_unit DECIMAL(10,2),
    discount_percent INT,
    order_date DATE,
    delivery_date DATE,
    payment_mode VARCHAR(30),
    order_status VARCHAR(30),
    rating INT
);

This table stores order related data like customer details, product info, dates, payments, and ratings.

Inserting Data into orders
INSERT INTO orders
(customer_name, city, product, category, quantity, price_per_unit, discount_percent, order_date, delivery_date, payment_mode, order_status, rating)
VALUES
('Amit Sharma', 'Delhi', 'Laptop', 'Electronics', 1, 65000, 10, '2025-01-05', '2025-01-08', 'Credit Card', 'Delivered', 5),
('Neha Verma', 'Mumbai', 'Headphones', 'Electronics', 2, 2500, 0, '2025-01-10', '2025-01-12', 'UPI', 'Delivered', 4),
('Rahul Khan', 'Delhi', 'Office Chair', 'Furniture', 1, 12000, 15, '2025-01-12', '2025-01-20', 'Debit Card', 'Delivered', 5),
('Priya Singh', 'Bangalore', 'Notebook', 'Stationery', 10, 80, 0, '2025-01-15', '2025-01-16', 'Cash', 'Delivered', 3),
('Arjun Mehta', 'Ahmedabad', 'Smartphone', 'Electronics', 1, 30000, 5, '2025-01-18', NULL, 'UPI', 'Cancelled', NULL),
('Sara Ali', 'Delhi', 'Table Lamp', 'Home Decor', 2, 1500, 20, '2025-01-20', '2025-01-23', 'Credit Card', 'Delivered', 4),
('Rohit Gupta', 'Mumbai', 'Water Bottle', 'Kitchen', 5, 500, 0, '2025-01-22', '2025-01-24', 'Cash', 'Delivered', 2),
('Kavita Joshi', 'Pune', 'Backpack', 'Accessories', 1, 3500, 10, '2025-01-25', '2025-01-29', 'Debit Card', 'Delivered', 5),
('Mohammed Faisal', 'Hyderabad', 'Keyboard', 'Electronics', 1, 1800, 0, '2025-01-28', '2025-02-01', 'UPI', 'Delivered', 4),
('Ananya Roy', 'Kolkata', 'Study Table', 'Furniture', 1, 15000, 25, '2025-02-01', NULL, 'Credit Card', 'Pending', NULL),
('Vikram Patel', 'Surat', 'Mixer Grinder', 'Appliances', 1, 4200, 5, '2025-02-03', '2025-02-06', 'UPI', 'Delivered', 4),
('Pooja Nair', 'Chennai', 'Yoga Mat', 'Fitness', 2, 1200, 0, '2025-02-05', '2025-02-07', 'Cash', 'Delivered', 5);

This adds sample data so we can practice real SQL queries.

Viewing the Data
SELECT * FROM orders;

Commonly Used MySQL Data Types
1.INT Stores whole numbers Example: age, quantity, ids

2.VARCHAR(n) Stores text with a fixed maximum length Example: name, email, city

3.DECIMAL(p,s) Stores precise decimal numbers Example: price, salary, total_spent
Precision (p): Total number of digits (maximum typically 38 or 39).
Scale (s): Number of digits to the right of the decimal point.
Formula: The maximum number of digits to the left of the decimal is p - s.
Example : DECIMAL(10, 3)
Can store 1234567.890 (10 total digits, 3 of which are to the right of the decimal). 

4. BOOLEAN Stores true or false values Example: is_active

5. DATE Stores only date Example: signup_date

6. DATETIME Stores date and time together Example: created_at

7. ENUM('val1', 'val2', ...) Stores one value from a predefined list Example: status ('active', 'inactive', 'pending')

* Removing the Table
After learning, we can delete the table.
-- DROP TABLE customers;
This removes the table completely from the database.

* Renaming the Table
-- ALTER TABLE customers RENAME TO clients;
What it does:

1. Renames the table instantly
2. Can rename multiple tables in one query
Example:
RENAME TABLE users TO customers,
             orders TO purchases;
✔ Very fast
✔ MySQL specific syntax
| Feature                        | RENAME TABLE | ALTER TABLE RENAME |
| ------------------------------ | ------------ | ------------------ |
| Works in MySQL                 | ✅            | ✅                  |
| Works in PostgreSQL            | ❌            | ✅                  |
| Rename multiple tables at once | ✅            | ❌                  |
| ANSI Standard SQL              | ❌            | ✅                  |

ALTER TABLE is more portable across databases
SYNTAX : ALTER TABLE table_name RENAME TO new_name;

RENAME TABLE is MySQL-style shortcut
