/*1. List all employees with their first name, last name and title.*/
SELECT 	FirstName , LastName
FROM employees;

/*2. List all employees from Seattle*/
SELECT 	FirstName , LastName
FROM employees
WHERE City =  'Seattle';

/*3. List all employees from London*/
SELECT 	FirstName , LastName
FROM employees
WHERE City =  'London';

/*4. List all employees that work in the Sales department*/
SELECT *
FROM employees
WHERE Title LIKE  '%Sales%';

# 5. List all females employees that work in the Sales department
SELECT *
FROM employees
WHERE Title LIKE  '%Sales%'
AND (TitleOfCourtesy ="Ms." 
OR  TitleOfCourtesy ="Mrs.");

SELECT *
FROM employees
WHERE Title LIKE  '%Sales%'
AND TitleOfCourtesy IN  'Ms','Mrs';

#6. List the 5 oldest employee
SELECT *
FROM employees
ORDER BY BirthDate ASC
LIMIT 5;

#7. List the first 5 hires of the company.
SELECT *
FROM employees
ORDER BY HireDate ASC
LIMIT 1,5;

#8. List the employee who reports to no one (the boss)
SELECT *
FROM employees
WHERE  ReportsTo  is NULL;

#9. List all employes by their first and last name, and the first and last name of the employees that they report to
SELECT a.FirstName , a.LastName,
b.FirstName,b.LastName
FROM employees a
JOIN employees  b 
ON a.ReportsTo=b.EmployeeID;

#10. Count all female employees.
SELECT COUNT(EmployeeID)
FROM employees
WHERE TitleOfCourtesy IN ('Ms.','Mrs.');

#11. Count all male employees
SELECT COUNT(EmployeeID)
FROM employees
WHERE TitleOfCourtesy IN ('Mr.','Dr.');

#12. Count how many employees are there from the different cities. For example, there are 4 employees from London.
SELECT City,COUNT(City)
FROM employees
GROUP BY City;

#13. List all OrderIDs and the employees (by first and last name) that have created them
SELECT FirstName, LastName
FROM employees
JOIN Orders
ON Orders.EmployeeID = Employees.EmployeeID;

#14 List all OrderIDs and the shipper name that the order is going to be shipped via.
SELECT OrderID , CompanyName
FROM Orders
JOIN Shippers
ON Orders.ShipVia = Shippers.ShipperID
#15 List all contries and the total number of orders that are going to be shipped there
SELECT ShipCountry , COUNT(ShipCountry) AS Orders
FROM Orders
GROUP BY ShipCountryl

#16. Find the employee that has served the most order
SELECT COUNT(OrderID) AS OrdersCount,FirstName
FROM Orders
JOIN Employees
ON Orders.EmployeeID = Employees.EmployeeID
GROUP BY Orders.EmployeeID
ORDER BY OrdersCount DESC
LIMIT 1;

#17. Find the customer that has placed the most orders
SELECT OrderID ,ContactName AS CustomerName,FirstName AS EmployeeFirstName
FROM Orders
JOIN Customers
ON  Orders.CustomerID = Customers.CustomerID
JOIN Employees
ON Orders.EmployeeID = Employees.EmployeeID;

#18.  List all orders, with the employee serving them and the customer, that has placed them.
SELECT OrderID, ContactName AS CustomerName, FirstName as EmployeeName
FROM Orders
JOIN Customers
ON Orders.CustomerID = Customers.CustomerID
JOIN Employees
ON Orders.EmployeeID = Employees.EmployeeID;

#19 List for which customer, which shipper is going to deliver the order.
SELECT a.ORDERID, b.CompanyName, c.CompanyName
FROM orders AS a
JOIN customers AS b
ON a.CustomerID = b.CustomerID
JOIN shippers AS c
ON a.ShipVia = c.ShipperID;