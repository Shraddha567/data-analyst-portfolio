* Updating & Deleting Data in a Table

-- Updating Rows
To modify existing data in a table, we use the UPDATE statement. Always use WHERE to avoid updating all rows by mistake.

* Updating a Single Row:
UPDATE orders
SET order_status = 'Delivered'
WHERE order_id = 10;

This updates the status of the order with order_id = 10.

* Updating Multiple Columns: 
UPDATE orders
SET discount_percent = 10,
    rating = 4
WHERE customer_name = 'Neha Verma';

This updates multiple columns for the matching row.

Updating Multiple Rows
UPDATE orders
SET order_status = 'Cancelled'
WHERE order_status = 'Pending';

This updates all pending orders to cancelled.

Updating Using a Condition
UPDATE orders
SET discount_percent = 20
WHERE category = 'Electronics' AND price_per_unit > 30000;

This applies a discount to expensive electronics.

Always Check Before Updating
SELECT *
FROM orders
WHERE order_status = 'Pending';

* Run a SELECT first to confirm which rows will be updated.

-- Deleting Rows
To remove data from a table, we use the DELETE statement. Always use WHERE to avoid deleting all rows by mistake.

* Deleting a Single Row
DELETE FROM orders
WHERE order_id = 5;

This deletes the order with order_id = 5.

* Deleting Multiple Rows
DELETE FROM orders
WHERE order_status = 'Cancelled';

This deletes all cancelled orders.

Deleting Using a Condition
DELETE FROM orders
WHERE order_date < '2025-01-10';

This deletes old orders placed before a specific date.

Always Check Before Deleting
SELECT *
FROM orders
WHERE order_status = 'Cancelled';

Run a SELECT first to confirm which rows will be deleted.

Deleting All Rows (Use Carefully)
DELETE FROM orders;

This removes all rows but keeps the table structure.

