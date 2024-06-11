#Tkinter 

#Tkinter is Python's standard library for creating Graphical User Interfaces (GUIs). It's a thin object-oriented layer on top of the Tcl/Tk GUI toolkit.

'''Basic Structure
A Tkinter application typically involves the following steps:

Importing Tkinter: Import the tkinter module.
Creating the main window: Create an instance of the Tk class.
Adding widgets: Add various widgets (buttons, labels, text fields, etc.) to the window.
Running the main event loop: Start the application's main loop, which waits for user interactions.'''

#SIMPLE TKINTER APPLICATION:
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Tkinter App")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Create a button widget
button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Button Clicked!"))
button.pack()

# Run the main event loop
root.mainloop()

#COMMONLY USED WIDGETS 
#Labels
#Labels are used to display text or images.
label = tk.Label(root, text="This is a label")
label.pack()

#Buttons
#Buttons can perform an action when clicked.
button = tk.Button(root, text="Click Me", command=some_function)
button.pack()

#Entry
#Entry widgets are used to accept single-line text input from the user.
entry = tk.Entry(root)
entry.pack()

#Text
#Text widgets are used for multi-line text input.
text = tk.Text(root)
text.pack()

#Frames
#Frames are used as containers to organize other widgets.
frame = tk.Frame(root)
frame.pack()



#Advanced Features
#Tkinter also supports more advanced features like creating menus, dialogs, canvases for drawing, and more.
menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


#The Canvas widget lets us display various graphics on the application. It can be used to draw simple shapes to complicated graphs. We can also display various kinds of custom widgets according to our needs.
'''C = Canvas(root, height, width, bd, bg, ..)'''
#Some common drawing methods:
#Creating an Oval
oval = C.create_oval(x0, y0, x1, y1, options)

#Creating an arc
arc = C.create_arc(20, 50, 190, 240, start=0, extent=110, fill="red")

#Creating a Line
line = C.create_line(x0, y0, x1, y1, ..., xn, yn, options)

#Creating a polygon
oval = C.create_polygon(x0, y0, x1, y1, ...xn, yn, options)

#EXAMPLE:
from tkinter import *


root = Tk()

C = Canvas(root, bg="yellow",
		height=250, width=300)

line = C.create_line(108, 120,
					320, 40,
					fill="green")

arc = C.create_arc(180, 150, 80,
				210, start=0,
				extent=220,
				fill="red")

oval = C.create_oval(80, 30, 140,
					150,
					fill="blue")

C.pack()
mainloop()

#LAYOUT MANAGERS 
#Layout Managers
#pack(): Packs widgets into a frame.
label.pack()
button.pack()

#grid(): Organizes widgets in a table-like structure.
label.grid(row=0, column=0)
entry.grid(row=0, column=1)

#place(): Places widgets at an absolute position.
label.place(x=50, y=50)