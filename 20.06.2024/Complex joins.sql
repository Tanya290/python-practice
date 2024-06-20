#Complex Joins
#Assuming we have three tables: `products`, `categories`, and `orders`.

#Tables: `products`,`categories`,`orders`

#Example of a Complex Join:

SELECT p.product_name, c.category_name, o.order_date, o.order_amount
FROM products p
JOIN categories c ON p.category_id = c.category_id
LEFT JOIN order_items oi ON p.product_id = oi.product_id
LEFT JOIN orders o ON oi.order_id = o.order_id
WHERE o.order_date > '2023-01-01' AND o.order_date < '2024-01-01';


#Subqueries

#Example of a Subquery:

SELECT 
    p.product_name, 
    (SELECT category_name FROM categories c WHERE c.category_id = p.category_id) AS category_name
FROM products p;


#Date-Time Functions
#Assuming we have the `orders` table with an `order_date` column.

#Extracting Parts of the Date:

SELECT 
    order_id, 
    EXTRACT(YEAR FROM order_date) AS order_year,
    EXTRACT(MONTH FROM order_date) AS order_month,
    EXTRACT(DAY FROM order_date) AS order_day
FROM orders;

#Formatting the Date:

SELECT 
    order_id, 
    TO_CHAR(order_date, 'YYYY-MM-DD') AS formatted_order_date
FROM orders;


#Additional Example for Clarification
#Complex Joins with Multiple Tables:


SELECT p.product_name, c.category_name, o.order_date, o.order_amount, u.user_name
FROM products p
JOIN categories c ON p.category_id = c.category_id
LEFT JOIN order_items oi ON p.product_id = oi.product_id
LEFT JOIN orders o ON oi.order_id = o.order_id
LEFT JOIN users u ON o.user_id = u.user_id
WHERE o.order_date > '2023-01-01' AND o.order_date < '2024-01-01';


#Subqueries with Aggregation:


SELECT 
    p.product_name, 
    (SELECT AVG(order_amount) FROM orders o JOIN order_items oi ON o.order_id = oi.order_id WHERE oi.product_id = p.product_id) AS avg_order_amount
FROM products p;
