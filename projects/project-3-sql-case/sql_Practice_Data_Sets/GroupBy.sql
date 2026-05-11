USE ecom;
-- SELECT city, COUNT(*) AS total_Count
-- FROM orders
-- GROUP BY city;

SELECT category, COUNT(*) As total_Orders, SUM(quantity * price_per_unit)
FROM orders
GROUP BY category;
