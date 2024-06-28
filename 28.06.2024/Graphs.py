#Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. 
#It is widely used in data science, machine learning, and scientific research for its ability to produce a wide range of plots and graphs with high customization options



#import matplotlib.pyplot as plt

# BASIC LINE PLOT
# Sample data
x = [0, 1, 2, 3, 4]
y = [1, 4, 9, 16, 25]

# Create a line plot
plt.plot(x, y, label='Squared Values', color='purple', marker='x')

# Add title and labels
plt.title('Basic Line Plot')
plt.xlabel('Input Value')
plt.ylabel('Squared Value')

# Add a legend
plt.legend()

# Show the plot
plt.show()

# SCATTER PLOT
# Sample data
x = [0, 1, 2, 3, 4]
y = [1, 4, 9, 16, 25]

# Create a scatter plot
plt.scatter(x, y, color='orange')

# Add title and labels
plt.title('Basic Scatter Plot')
plt.xlabel('Input Value')
plt.ylabel('Squared Value')

# Show the plot
plt.show()

# BAR CHART
# Sample data
categories = ['X', 'Y', 'Z', 'W']
values = [5, 15, 25, 35]

# Create a bar chart
plt.bar(categories, values, color='blue')

# Add title and labels
plt.title('Basic Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')

# Show the plot
plt.show()

# PIE CHART
# Sample data
labels = ['X', 'Y', 'Z', 'W']
sizes = [20, 25, 35, 20]
colors = ['lightblue', 'lightgreen', 'lightpink', 'lightyellow']
explode = (0, 0.1, 0, 0)  # explode the 2nd slice (Y)

# Create a pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Add title
plt.title('Basic Pie Chart')

# Show the plot
plt.show()
