-- CREATE DATABASE ecom;
-- USE ecom;
CREATE TABLE orders ( 
order_id INT primary key auto_increment,
customer_name varchar(100),
city varchar(50),
product varchar(50),
category varchar(50),
quantity INT,
price_per_unit DECIMAL(10.2),
discount_percent INT,
order_date DATE,
delivery_date DATE,
payment_mode VARCHAR(30),
order_status VARCHAR(30),
rating int
);