-- Create the database
CREATE DATABASE myntra;

-- Use the database
USE myntra;

-- Create the products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2),
    category VARCHAR(50)
);

-- Create the payment table
CREATE TABLE payment (
    payment_id INT PRIMARY KEY,
    order_id INT,
    payment_date DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES `order`(order_id)
);

-- Create the customer table
CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15)
);

-- Create the order table
CREATE TABLE `order` (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    product_id INT,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);


-- Insert data into the products table
INSERT INTO products (product_id, product_name, price, category) VALUES
(1, 'T-Shirt', 500.00, 'Apparel'),
(2, 'Jeans', 1200.00, 'Apparel'),
(3, 'Sneakers', 3000.00, 'Footwear');

-- Insert data into the customer table
INSERT INTO customer (customer_id, customer_name, email, phone) VALUES
(1, 'Doe', 'doe@example.com', '1234567890'),
(2, 'Jane', 'jane@example.com', '0987654321');

-- Insert data into the order table
INSERT INTO `order` (order_id, customer_id, order_date, product_id) VALUES
(1, 1, '2024-06-01', 1),
(2, 1, '2024-06-02', 2),
(3, 2, '2024-06-03', 3);

-- Insert data into the payment table
INSERT INTO payment (payment_id, order_id, payment_date, amount) VALUES
(1, 1, '2024-06-01', 500.00),
(2, 2, '2024-06-02', 1200.00),
(3, 3, '2024-06-03', 3000.00);


#Inner Join
#Get a list of customers who have placed orders along with the product details:

SELECT c.customer_name, c.email, o.order_id, p.product_name, p.price
FROM customer c
INNER JOIN `order` o ON c.customer_id = o.customer_id
INNER JOIN products p ON o.product_id = p.product_id;

#Left Join
#Get a list of all customers and their orders (if any), including those customers who have not placed any orders:

SELECT c.customer_name, c.email, o.order_id, p.product_name, p.price
FROM customer c
LEFT JOIN `order` o ON c.customer_id = o.customer_id
LEFT JOIN products p ON o.product_id = p.product_id;

#Right Join
#Get a list of all orders and the customers who placed them, including orders that may not have customer information:

SELECT c.customer_name, c.email, o.order_id, p.product_name, p.price
FROM `order` o
RIGHT JOIN customer c ON c.customer_id = o.customer_id
RIGHT JOIN products p ON o.product_id = p.product_id;


#Full Join
#Get a complete list of customers and orders, including those customers who haven't placed any orders and orders that don't have customer information:


SELECT c.customer_name, c.email, p.product_name, p.price
FROM customer c
LEFT JOIN `order` o ON c.customer_id = o.customer_id
LEFT JOIN products p ON o.product_id = p.product_id
UNION
SELECT c.customer_name, c.email, p.product_name, p.price
FROM products p
LEFT JOIN `order` o ON o.product_id = p.product_id
LEFT JOIN customer c ON o.customer_id = c.customer_id;


#Cross Join
#Get a Cartesian product of customers and products (every customer paired with every product):

SELECT c.customer_name, c.email, p.product_name, p.price
FROM customer c
CROSS JOIN products p;
