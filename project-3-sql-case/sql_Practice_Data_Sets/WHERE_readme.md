Selecting Data from the orders Table
To read data from a table, we use the SELECT statement.

Selecting All Columns
SELECT * FROM orders;

This returns all rows and all columns from the orders table.

Selecting Specific Columns
SELECT customer_name, product, city
FROM orders;

This returns only the selected columns.

Filtering Rows Using WHERE
SELECT *
FROM orders
WHERE city = 'Delhi';

This returns orders placed from Delhi.

Using Conditions
SELECT customer_name, product, price_per_unit
FROM orders
WHERE price_per_unit > 5000;

This returns expensive products.

Here is another example using not equal to:

SELECT customer_name, product, price_per_unit
FROM orders
WHERE price_per_unit != 5000;

In SQL, we use IS NULL instead of = NULL because NULL represents an unknown or missing value, not an actual value, and any comparison using operators like =, !=, <, or > with NULL always results in UNKNOWN rather than TRUE or FALSE. Since a WHERE clause only selects rows where the condition evaluates to TRUE, expressions like column = NULL or column != NULL never return any rows. IS NULL and IS NOT NULL are special SQL conditions designed specifically to check whether a column has no value, avoiding this ambiguity and correctly identifying missing data.

SELECT *
FROM orders
WHERE delivery_date IS NULL;

Using AND and OR
SELECT *
FROM orders
WHERE city = 'Delhi' AND order_status = 'Delivered';

This returns delivered orders from Delhi.

Sorting Data
SELECT customer_name, order_date, price_per_unit
FROM orders
ORDER BY order_date DESC;

This sorts orders by latest first.