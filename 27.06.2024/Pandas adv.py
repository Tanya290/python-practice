
#Pandas: An Overview
#Pandas is an open-source data manipulation and analysis library built on top of the Python programming language. It provides fast, flexible, and expressive data structures designed to make working with structured (tabular, multidimensional, potentially heterogeneous) and time-series data both easy and intuitive. Pandas is a cornerstone for data analysis in Python, widely used in data science, machine learning, scientific computing, and many other fields.

#Key Data Structures

#Series
#A one-dimensional labeled array capable of holding any data type (integers, strings, floating-point numbers, Python objects, etc.). The labels are known as the index.

import pandas as pd

# Creating a Series from a list
s = pd.Series([1, 3, 5, None, 6, 8])
print(s)

# Creating a Series from a dictionary
s = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(s)


#Output:
#0    1.0
#1    3.0
#2    5.0
#3    NaN
#4    6.0
#5    8.0
#dtype: float64
#a    1
#b    2
#c    3
#dtype: int64


#DataFrame
#A two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns). Can be thought of as a dictionary of Series objects.


# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)
print(df)

# Creating a DataFrame from a list of dictionaries
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'San Francisco'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Los Angeles'}
]

df = pd.DataFrame(data)
print(df)


#Output:

#      Name  Age           City
#0    Alice   25       New York
#1      Bob   30  San Francisco
#2  Charlie   35    Los Angeles
#      Name  Age           City
#0    Alice   25       New York
#1      Bob   30  San Francisco
#2  Charlie   35    Los Angeles


#Basic Operations

#Indexing and Selecting Data

#Selecting a Column
#we can select a column from a DataFrame using the column label.


# Selecting a column
ages = df['Age']
print(ages)


#Output:

#0    25
#1    30
#2    35
#Name: Age, dtype: int64


#Selecting Rows by Label
#Use the `loc` attribute for label-based indexing.


# Selecting rows by label
row = df.loc[0]
print(row)

rows = df.loc[0:1]
print(rows)


#Output:

#Name       Alice
#Age           25
#City    New York
#Name: 0, dtype: object
#    Name  Age           City
#0  Alice   25       New York
#1    Bob   30  San Francisco


#Filtering Data
#Filtering allows you to select rows that meet certain conditions.


# Selecting rows where Age > 30
filtered_df = df[df['Age'] > 30]
print(filtered_df)


#Output:
#      Name  Age         City
#2  Charlie   35  Los Angeles


#Advanced Data Operations

#Grouping and Aggregation

#Grouping and aggregation are useful for summarizing data.


# Group by 'City' and calculate the mean of each group
grouped = df.groupby('City').mean()
print(grouped)


#Output:

#               Age
#City              
#Los Angeles    35.0
#New York       25.0
#San Francisco  30.0


#Merging and Joining
#we can merge or join data from different DataFrames.

# Creating another DataFrame
data2 = {
    'Name': ['Alice', 'Bob', 'David'],
    'Salary': [50000, 60000, 70000]
}

df2 = pd.DataFrame(data2)

# Merging DataFrames on a common column
merged_df = pd.merge(df, df2, on='Name')
print(merged_df)


#Output:

#     Name  Age           City  Salary
#0   Alice   25       New York   50000
#1     Bob   30  San Francisco   60000


#Reshaping Data

#Pandas provides functions for reshaping data.

#Pivot
#Reshape data where columns become rows and vice versa.


# Creating a sample DataFrame
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'City': ['New York', 'San Francisco', 'Los Angeles'],
    'Temperature': [30, 40, 50]
}

df = pd.DataFrame(data)

# Pivoting the DataFrame
pivoted_df = df.pivot(index='Date', columns='City', values='Temperature')
print(pivoted_df)


#Output:

#City       Los Angeles  New York  San Francisco
#Date                                           
#2024-01-01           NaN       30.0            NaN
#2024-01-02           NaN        NaN           40.0
#2024-01-03          50.0        NaN            NaN


#Data Visualization

#Pandas integrates well with Matplotlib for data visualization.

import matplotlib.pyplot as plt

# Creating a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}

df = pd.DataFrame(data)

# Plotting a DataFrame
df.plot(kind='bar', x='Name', y='Salary')
plt.show()

#So in Conclusion:
#Pandas is a powerful and flexible library for data manipulation and analysis. Its core data structures, the Series and DataFrame, make it easy to work with structured data. With functionalities for indexing, selecting, filtering, grouping, merging, reshaping, and visualizing data, Pandas is essential for data analysis in Python.