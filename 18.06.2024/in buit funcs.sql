
#String Functions
#1.CONCAT()
#Concatenates two or more strings.

SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM employees;

#Concatenates `first_name` and `last_name` columns with a space in between to form the full name.

#2.LOWER()
#Converts a string to lower case.

SELECT LOWER(first_name) AS lower_case_first_name
FROM employees;

#Converts the `first_name` values to lower case.

#3.UPPER()
#Converts a string to upper case.

SELECT UPPER(last_name) AS upper_case_last_name
FROM employees;

#Converts the `last_name` values to upper case.

#4.LENGTH()
#Returns the length of a string.

SELECT first_name, LENGTH(first_name) AS name_length
FROM employees;

#Returns the number of characters in each value of the `first_name` column.

#5.SUBSTRING() or SUBSTR()
#Extracts a substring from a string.


SELECT SUBSTRING(first_name, 1, 2) AS first_two_letters
FROM employees;

#Extracts the first two characters from the `first_name` values.

#6.REPLACE()
#Replaces all occurrences of a specified substring with another substring.

SELECT REPLACE(first_name, 'a', 'A') AS replaced_name
FROM employees;

#Replaces all occurrences of the letter 'a' with 'A' in the `first_name` values.

#7.TRIM()
#Removes leading and trailing spaces from a string.

SELECT TRIM('silia doe') AS trimmed_name;

#Removes the leading and trailing spaces from the string '  John Doe  '.

#8.LTRIM()
#Removes leading spaces from a string.

SELECT LTRIM('silia doe') AS left_trimmed_name;
#Removes the leading spaces from the string '  John Doe'.

#9.RTRIM()
#Removes trailing spaces from a string.

SELECT RTRIM('silia doe  ') AS right_trimmed_name;

#Removes the trailing spaces from the string 'John Doe  '.

#10.INSTR()
#Returns the position of the first occurrence of a substring in a string.

SELECT INSTR(first_name, 'a') AS position_of_a
FROM employees;


#Returns the position of the first occurrence of the letter 'a' in the `first_name` values.

#11.LEFT() and RIGHT()
#Extracts a specified number of characters from the left or right side of a string.

SELECT LEFT(first_name, 3) AS first_three_letters,
       RIGHT(last_name, 3) AS last_three_letters
FROM employees;

#`LEFT(first_name, 3)`: Extracts the first three characters from the `first_name` values.
#`RIGHT(last_name, 3)`: Extracts the last three characters from the `last_name` values.

#SQRT(number): This function returns the square root of a non-negative number.

SELECT SQRT(25) AS result; 
#Output: 5

#FLOOR(number): This function returns the largest integer value that is less than or equal to the given number.

SELECT FLOOR(3.8) AS result; 
#Output: 3

SELECT FLOOR(-3.8) AS result; 
#Output: -4

#ROUND(number, [decimals]): This function rounds a number to a specified number of decimal places. 
#If decimals is omitted, it rounds to the nearest integer.
SELECT ROUND(3.1416, 2) AS result; 
#Output: 3.14

SELECT ROUND(3.1416) AS result; 
#Output: 3