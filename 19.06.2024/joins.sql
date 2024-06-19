
#In SQL, a join is a means for combining columns from two or more tables based on a related column between them.
#Joins are fundamental for relational databases as they allow you to retrieve related data spread across multiple tables efficiently.

#1.INNER JOIN
#Returns records that have matching values in both tables.

SELECT Orders.OrderID, Customers.CustomerName, Items.ItemName, Items.ItemPrice
FROM Orders
INNER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
INNER JOIN Items ON OrderDetails.ItemID = Items.ItemID;


#2.LEFT JOIN (or LEFT OUTER JOIN)
#Returns all records from the left table, and the matched records from the right table. If no match is found, NULL values are returned for columns from the right table.

SELECT Orders.OrderID, Customers.CustomerName, Items.ItemName, Items.ItemPrice
FROM Orders
LEFT JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
LEFT JOIN Customers ON Orders.CustomerID = Customers.CustomerID
LEFT JOIN Items ON OrderDetails.ItemID = Items.ItemID;


#3.RIGHT JOIN (or RIGHT OUTER JOIN)
#Returns all records from the right table, and the matched records from the left table. If no match is found, NULL values are returned for columns from the left table.

SELECT Orders.OrderID, Customers.CustomerName, Items.ItemName, Items.ItemPrice
FROM Orders
RIGHT JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
RIGHT JOIN Customers ON Orders.CustomerID = Customers.CustomerID
RIGHT JOIN Items ON OrderDetails.ItemID = Items.ItemID;


#4.FULL JOIN (or FULL OUTER JOIN)
#Returns all records when there is a match in either left or right table. If there is no match, the result is NULL on the side where there is no match.

SELECT Orders.OrderID, Customers.CustomerName, Items.ItemName, Items.ItemPrice
FROM Orders
FULL OUTER JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
FULL OUTER JOIN Customers ON Orders.CustomerID = Customers.CustomerID
FULL OUTER JOIN Items ON OrderDetails.ItemID = Items.ItemID;


#5.CROSS JOIN
#Returns the Cartesian product of the two tables. Each row from the first table is combined with all rows in the second table.

SELECT Customers.CustomerName, Items.ItemName
FROM Customers
CROSS JOIN Items;


#6.SELF JOIN
#Joins a table with itself. This is useful for hierarchical data.

SELECT e1.CustomerName AS Customer, e2.CustomerName AS Referrer
FROM Customers e1
INNER JOIN Customers e2 ON e1.ReferrerID = e2.CustomerID;


#7.NATURAL JOIN
#Based on all columns in the two tables that have the same name and selects rows with equal values in the relevant columns.

SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
NATURAL JOIN Customers;
