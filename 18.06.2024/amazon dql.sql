create database amazon;
use amazon;

#GROUP BY
#The GROUP BY clause groups rows that have the same values in specified columns into aggregated data.

#Example: Total Order Amount Per Customer

SELECT customer_id, SUM(order_amount) AS total_amount
FROM orders
GROUP BY customer_id;

#ORDER BY
#The ORDER BY clause sorts the result set by one or more columns.

#Example: Total Order Amount Per Customer, Ordered by Total Amount

SELECT customer_id, SUM(order_amount) AS total_amount
FROM orders
GROUP BY customer_id
ORDER BY total_amount DESC;

#HAVING
#The HAVING clause filters groups based on a condition.

#Example: Customers with Total Order Amount Greater than $50

SELECT customer_id, SUM(order_amount) AS total_amount
FROM orders
GROUP BY customer_id
HAVING SUM(order_amount) > 50;

#Example: Customers with Total Order Amount Greater than $50, Ordered by Total Amount

SELECT customer_id, SUM(order_amount) AS total_amount
FROM orders
GROUP BY customer_id
HAVING SUM(order_amount) > 50
ORDER BY total_amount DESC;

#Example: Total Quantity and Order Amount Per Customer Per Product, Filtered and Ordered

SELECT customer_id, product_id, SUM(quantity) AS total_quantity, SUM(order_amount) AS total_amount
FROM orders
GROUP BY customer_id, product_id
HAVING SUM(quantity) > 5
ORDER BY total_quantity DESC;

