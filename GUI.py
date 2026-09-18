"""
Tkinter GUI Basics

This script provides an introduction to Tkinter widgets and their common methods and arguments.
It also demonstrates basic layout management using the `pack` and `grid` geometry managers.

Widgets covered:
- Button
- Label
- Entry
- Text
- Frame

Grid Layout Example included at the end.
"""

import tkinter as tk

# Initialize the main application window
app = tk.Tk()
app.title("Tkinter Widgets Example")  # Set the window title


# ==============================
# Button Widget
# ==============================
# The Button widget is used to create clickable buttons.

def button_click():
    print("Button clicked!")


button = tk.Button(app,
                   text="Click Me",  # Label of the button
                   command=button_click,  # Function to call when the button is clicked
                   bg="blue",  # Background color
                   fg="white",  # Foreground (text) color
                   font=("Arial", 12),  # Font type and size
                   width=10,  # Width of the button
                   height=2,  # Height of the button
                   relief=tk.RAISED)  # Button border style
button.pack()  # Add the button to the window

# ==============================
# Label Widget
# ==============================
# The Label widget is used to display text or images.

label = tk.Label(app,
                 text="Hello, Tkinter!",  # Text to display
                 bg="yellow",  # Background color
                 fg="black",  # Foreground (text) color
                 font=("Helvetica", 14),  # Font type and size
                 width=20,  # Width of the label
                 height=3,  # Height of the label
                 padx=10,  # Horizontal padding
                 pady=10)  # Vertical padding
label.pack()  # Add the label to the window

# ==============================
# Entry Widget
# ==============================
# The Entry widget is used for single-line text input.

entry = tk.Entry(app,
                 show="*",  # Character to display instead of actual input (e.g., for passwords)
                 bg="lightgray",  # Background color
                 fg="black",  # Foreground (text) color
                 font=("Courier", 12),  # Font type and size
                 width=30,  # Width of the entry box
                 relief=tk.SUNKEN)  # Border style
entry.pack()  # Add the entry widget to the window

# ==============================
# Text Widget
# ==============================
# The Text widget is used for multi-line text input.

text = tk.Text(app,
               wrap=tk.WORD,  # Text wrapping mode
               bg="white",  # Background color
               fg="black",  # Foreground (text) color
               font=("Times", 12),  # Font type and size
               width=40,  # Width of the text area
               height=10)  # Height of the text area
text.pack()  # Add the text widget to the window

# ==============================
# Frame Widget
# ==============================
# The Frame widget is used as a container to organize other widgets.

frame = tk.Frame(app,
                 bg="gray",  # Background color
                 width=300,  # Width of the frame
                 height=200,  # Height of the frame
               )  # Border width
frame.pack()  # Add the frame to the window


# ==============================


# Grid Layout Example
# ==============================
# Using the grid geometry manager to organize widgets in a table-like structure.

# Create a new frame for grid layout example
grid_frame = tk.Frame(app)
grid_frame.pack()

# Add labels to the grid
tk.Label(grid_frame, text="Name:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(grid_frame, text="Email:").grid(row=1, column=0, padx=10, pady=10)

# Add entry widgets to the grid
tk.Entry(grid_frame).grid(row=0, column=1, padx=10, pady=10)
tk.Entry(grid_frame).grid(row=1, column=1, padx=10, pady=10)

# Add a submit button
tk.Button(grid_frame, text="Submit").grid(row=2, column=1, padx=10, pady=10)

# Start the main event loop
app.mainloop()



"""

                    ______________________
                    <<READ BEFORE START>>
                    ______________________


We built our calculator's GUI following these steps:

1- create an empty window object from the class TK()
2- define title, geometry and resizing options
3- modify style by changing the background and the window icon
4- creating 2 frames and packing them to be up to each other
5- give each of them expand and fill options to adjust to the available space on the screen
6- in the upper frame, add 2 labels up to each other and give them the expand and fill options
7- in the lower frame, create a button object with predefined properties, add it to the parent frame as a grid
8- loop over this gridded button as many times as the number of buttons to be added (which are defined previously as a list of tuplels)
9- add color options for the "=" button before object construction (note the green color property is set before passing button_properties to the button object)
10- add configuration to each column and row to mae all buttons expand to fill the cells containing them
11- loop over the GUI (window.mainloop()) to keep it being rendered

The sticky= 'ewns' means to make each button sticks to its neighbour button from east, west, north and south
Try to comment lines and removing attributes to observe their effect
Try to rebuild the GUI from scratch in a separate file
Try changing styles: colors (use any online color picker tool) fonts (u have to have the font downloaded to be able to use it, u can just stick to "Arial" for now)

                            _________
                            IMPORTANT
                            _________

recap those topics (needed in the next lecture):
1- functions definition and use
2- lambda function
3- if, else and elif statements
4- try-except
5- string methods like split() and replace()

"""



import tkinter as tk

# Create the main application window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x667")
window.resizable(False, False) # make window non-resizable
window.configure(bg="#121212")  # Dark background color
window.iconbitmap(r"C:\Users\SHIBA_LION\Desktop\my books\python\python projects\icon.ico") # must always be .ico extension
# Create a frame for the display
display_frame = tk.Frame(window, bg="#1e1e1e")
display_frame.pack( expand=True, fill="both") # makes frame adjust to the available space in its parent(window)
# fill also has 2 other values, "x" and "y"


# Create a label to display the total expression
total_label = tk.Label(display_frame, text="", anchor=tk.E, bg="#1e1e1e", fg="#a0a0a0", padx=24, font=("Arial", 16))
total_label.pack(expand=True, fill="both") # makes label adjust to the available space in its parent (upper frame)

# Create another label to display the current expression
label = tk.Label(display_frame, text="", anchor=tk.E, bg="#1e1e1e", fg="#e0e0e0", padx=24, font=("Arial", 40, "bold"))
label.pack(expand=True, fill="both") # makes label adjust to the REMAINING available space in its parent (upper frame)

# Create a frame for the buttons
buttons_frame = tk.Frame(window, bg="#1e1e1e")
buttons_frame.pack(expand=True, fill="both") # makes button frame adjust to the remaining space in its parent (window)

# Define button properties in a single package (dictionary)
button_properties = {
    'width': 5, 'height': 2, 'bg': "#2e2e2e", 'fg': "#e0e0e0", 'font': ("Arial", 18), 'borderwidth': 0
}


# Buttons definition

buttons = [
    ('C', 0, 0), ('√', 0, 1), ('x²', 0, 2), ('÷', 0, 3),
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('×', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
    ('.', 4, 0), ('0', 4, 1), ('=', 4, 2, 2)  # '=' button spans two columns
]

# Create buttons and add them to the grid
for button in buttons:
    text = button[0]
    row = button[1]
    column = button[2]
    columnspan = button[3] if len(button) == 4 else 1

    """
      if len(button) == 4:
        columnspan = button[3]
    else:columnspan =  1
    """



    # Use a different color for the '=' button
    if text == '=':
        button_properties['bg'] = "#4caf50"  # Green background for '=' button
        button_properties['fg'] = "#ffffff"  # White text for '=' button

    # start creating the button object after defining needed properties and features above
    tk.Button(buttons_frame, text=text, **button_properties).grid(row=row, column=column, columnspan=columnspan, sticky= 'wnes')
    # sticky can take any value as a combination of (e, w, n, s). ex: "we", "se" , "wns", "s"

# Make buttons expand to fill the grid cells
for i in range(5): # expand the 5 rows
    buttons_frame.grid_rowconfigure(i, weight=1)
for j in range(4): # expand the 4 columns
    buttons_frame.grid_columnconfigure(j, weight=1)



# Start the Tkinter event loop
window.mainloop()


