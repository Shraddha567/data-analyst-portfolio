-- SELECT * FROM orders WHERE discount_percent = 20;
-- SELECT * FROM orders WHERE discount_percent > 20;
-- SELECT customer_name, city, quantity FROM orders WHERE discount_percent < 20;
-- SELECT * FROM orders WHERE delivery_date IS NULL;
SELECT customer_name, order_date, price_per_unit FROM orders ORDER BY order_date DESC;