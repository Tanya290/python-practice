# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is widely used for its flexibility and ease of use, enabling the creation of a wide range of plots, from simple line graphs to complex multi-plot layouts.

#Here are some key features of Matplotlib:

#Variety of Plots: Supports numerous types of plots such as line plots, scatter plots, bar charts, histograms, pie charts, error bars, box plots, and more.
#Customization: Offers extensive customization options for plots, including color, line style, markers, labels, and annotations.
#Interactive Figures: Allows for the creation of interactive plots that can be zoomed, panned, and updated in real-time.
#Integration: Works well with other libraries such as NumPy, pandas, and seaborn. It also integrates with GUI toolkits like Tkinter, Qt, and wxPython.
#Publication Quality: Capable of producing high-quality figures suitable for publication.
#Subplots: Supports complex layouts with multiple subplots in a single figure.

## Examples of Matplotlib Plots

### Simple Line Plot


import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create a line plot
plt.plot(x, y, label='Squared Values', color='green', marker='s')

# Add title and labels
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a legend
plt.legend()

# Show the plot
plt.show()


#Advanced Features

#1. 3D Plotting

#Using the `mpl_toolkits.mplot3d` module, you can create 3D plots.

from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Sample data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Add title and labels
ax.set_title('3D Surface Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Show the plot
plt.show()


#2. Animations

#Matplotlib can create animations using the `FuncAnimation` class from `matplotlib.animation`.


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Sample data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a figure and axis
fig, ax = plt.subplots()
line, = ax.plot(x, y)

# Update function for animation
def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))
    return line,

# Create an animation
anim = FuncAnimation(fig, update, frames=range(100), interval=50)

# Show the plot
plt.show()

#3. Customizing Styles

#Use `plt.style.use('style_name')` to change the appearance of plots.

import matplotlib.pyplot as plt

# Apply a style
plt.style.use('seaborn-darkgrid')

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# Create a bar chart
plt.bar(categories, values, color='skyblue')

# Add title and labels
plt.title('Styled Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show the plot
plt.show()
