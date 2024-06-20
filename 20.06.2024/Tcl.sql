/* TCL commands are used to manage transactions in the database.
A transaction is a sequence of one or more SQL operations that are executed as a single unit of work.
The main TCL commands are COMMIT, ROLLBACK, and SAVEPOINT. */

/* COMMIT
The COMMIT command is used to save all changes made during the current transaction.
Once a transaction is committed, the changes are permanent and visible to other users. */
#BEGIN TRANSACTION;
UPDATE products SET price = price * 1.10 WHERE category = 'Electronics';
COMMIT;

/* ROLLBACK
The ROLLBACK command is used to undo changes made during the current transaction.
It can revert the database to the state it was in before the transaction began. */
#BEGIN TRANSACTION;
UPDATE products SET price = price * 1.10 WHERE category = 'Electronics';
ROLLBACK;

/* SAVEPOINT
The SAVEPOINT command sets a point within a transaction to which you can later roll back.
This allows partial rollbacks within a transaction. */
#BEGIN TRANSACTION;
UPDATE products SET price = price * 1.10 WHERE category = 'Electronics';
SAVEPOINT before_discount_update;
UPDATE products SET discount = discount * 1.15 WHERE category = 'Electronics';
ROLLBACK TO SAVEPOINT before_discount_update;
COMMIT;

/* Triggers
A trigger is a stored procedure in a database that automatically invokes whenever a specified event occurs.
Triggers are used to maintain the integrity of the information on the database.
Creating a Trigger:
Triggers can be created to run before or after an INSERT, UPDATE, or DELETE operation on a table. */

DELIMITER //
CREATE TRIGGER product_price_update
BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
    IF NEW.price < OLD.price THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Price cannot be decreased!';
    END IF;
END;
//
DELIMITER ;

/* Trigger Example */
DELIMITER //
CREATE TRIGGER log_product_changes
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (product_id, old_price, new_price, change_date)
    VALUES (OLD.product_id, OLD.price, NEW.price, NOW());
END;
//
DELIMITER ;

/* Views
A view is a virtual table based on the result set of an SQL query. It can contain all rows of a table or select rows from a table.
Views are used to simplify complex queries, enhance security, and provide a layer of abstraction.

Creating a View
The CREATE VIEW command is used to create a view. */

CREATE VIEW electronics_view AS
SELECT product_id, product_name, category, price
FROM products
WHERE category = 'Electronics';

/* Using a View
Once created, a view can be queried like a regular table */
SELECT * FROM electronics_view;

/* Updating a View
Some views are updatable, which means you can use them to insert, update, and delete rows in the underlying table. */
UPDATE electronics_view
SET price = price * 1.10
WHERE product_id = 101;

/* Dropping a View
To delete a view, use the DROP VIEW command. */
DROP VIEW electronics_view;
