-- Create the myntra database
CREATE DATABASE myntra;

-- Switch to the myntra database
USE myntra;

-- Create a table for customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    phone_number VARCHAR(20)
);

-- Create a table for products
CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2),
    stock_quantity INT
);

-- Create a table for orders
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create a table for payments
CREATE TABLE IF NOT EXISTS payments (
    payment_id INT PRIMARY KEY,
    order_id INT,
    amount DECIMAL(10, 2),
    payment_date DATE,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- Insert some sample data into the tables
INSERT INTO customers (customer_name, email, phone_number) VALUES
('John Doe', 'john@example.com', '123-456-7890'),
('Jane Smith', 'jane@example.com', '987-654-3210');

INSERT INTO products (product_name, category, price, stock_quantity) VALUES
('T-shirt', 'Men', 19.99, 100),
('Jeans', 'Men', 39.99, 50),
('Dress', 'Women', 49.99, 80),
('Shoes', 'Women', 29.99, 120),
('Sunglasses', 'Accessories', 9.99, 200);

INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 1, 2, '2024-06-14'),
(2, 3, 1, '2024-06-15'),
(1, 5, 3, '2024-06-16');

INSERT INTO payments (order_id, amount, payment_date) VALUES
(1, 59.97, '2024-06-15'),
(2, 49.99, '2024-06-16'),
(3, 29.97, '2024-06-17');

-- Count the number of customers
SELECT COUNT(*) AS num_customers FROM customers;

-- Count the number of products
SELECT COUNT(*) AS num_products FROM products;

-- Count the number of orders
SELECT COUNT(*) AS num_orders FROM orders;

-- Count the number of payments
SELECT COUNT(*) AS num_payments FROM payments;

-- Calculate the total sales value
SELECT SUM(price * quantity) AS total_sales_value FROM orders JOIN products ON orders.product_id = products.product_id;

-- Find the average price of products
SELECT AVG(price) AS average_price FROM products;

-- Find the most expensive product
SELECT * FROM products WHERE price = (SELECT MAX(price) FROM products);

-- Find the cheapest product
SELECT * FROM products WHERE price = (SELECT MIN(price) FROM products);

-- Add a new column for discount to the products table
ALTER TABLE products
ADD COLUMN discount DECIMAL(5, 2);

-- Insert some sample data into the new column
UPDATE products SET discount = 0.10 WHERE category = 'Men';
UPDATE products SET discount = 0.15 WHERE category = 'Women';

-- View the updated table structure
DESCRIBE products;

-- Drop the discount column from the products table
ALTER TABLE products
DROP COLUMN discount;



