#What is Pandas?
#Pandas is a powerful, open-source data manipulation and analysis library for Python. It provides easy-to-use data structures and data analysis tools for handling structured data, such as data tables (dataframes) and time series.


#Key Features of Pandas

#1.Data Structures:
#Series: A one-dimensional labeled array capable of holding any data type.
#DataFrame**: A two-dimensional labeled data structure with columns of potentially different types, similar to a spreadsheet or SQL table.

#2.Data Manipulation:
#   - Selection: Access specific rows and columns.
#   - Filtering: Filter data based on conditions.
#   - Aggregation: Perform operations like mean, sum, and count on data groups.
#   - Merging: Combine data from multiple dataframes.

#3.Handling Missing Data:
#   - Drop: Remove rows or columns with missing values.
#   - Fill: Fill missing values with specified values or methods.

#4.Time Series Handling:
#   - Date Range Generation: Create ranges of dates for indexing.
#   - Resampling: Change the frequency of your time series data.

#5. File I/O:
#   - Reading: Read data from files (CSV, Excel, SQL, etc.).
#   - Writing: Write data to files.

#6.Data Visualization:
#   - Plotting: Generate plots and visualizations directly from dataframes.

#Examples of What You Can Do with Pandas

#1.Importing Pandas

import pandas as pd


#2.Creating a Series
#A Series is a one-dimensional array-like object containing data and an associated array of labels (index).


import numpy as np
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)


#3.Creating a DataFrame
#A DataFrame is a two-dimensional data structure with labeled axes (rows and columns).


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'San Francisco', 'Los Angeles']
}

df = pd.DataFrame(data)
print(df)

#4.Reading and Writing Data
#we can read from and write to various file formats.


# Reading data from a CSV file
df = pd.read_csv('data.csv')

# Writing data to a CSV file
df.to_csv('output.csv', index=False)

#5.Data Manipulation
#Selecting, filtering, grouping, and handling missing data.


# Selecting a column
ages = df['Age']

# Filtering rows based on a condition
filtered_df = df[df['Age'] > 30]

# Grouping and aggregating data
grouped = df.groupby('City').mean()

# Handling missing data
df = df.dropna()  # Drop rows with any missing values
df = df.fillna(0)  # Fill missing values with 0

#6.Working with Time Series
#Creating and manipulating time series data.


# Creating a date range
rng = pd.date_range('2024-01-01', periods=10, freq='D')
print(rng)

# Creating a DataFrame with a time index
ts = pd.Series(np.random.randn(10), index=rng)
print(ts)


#7.Basic Operations
#Indexing, selecting, and filtering data.


# Selecting a column
ages = df['Age']
print(ages)

# Selecting rows by label
row = df.loc[0]  # First row
print(row)

rows = df.loc[0:1]  # First two rows
print(rows)

# Filtering data
filtered_df = df[df['Age'] > 30]
print(filtered_df)


#8.Visualization
#Integrating with Matplotlib for data visualization.


import matplotlib.pyplot as plt

# Plotting a DataFrame
df.plot(kind='bar')
plt.show()
