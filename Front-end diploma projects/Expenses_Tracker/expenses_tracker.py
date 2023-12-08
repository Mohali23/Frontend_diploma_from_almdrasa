
# Import necessary libraries
import requests  # Importing requests module to make HTTP requests
from tkinter import *  # Importing all classes from tkinter module
from tkinter import ttk  # Importing ttk class from tkinter module

# Define font styles and sizes
font_family = 'Bahnschrift'
main_font_size = 20
input_font_size = 13

# Create Tkinter window
root = Tk()

# Window size and title
window_width = 1000
window_height = 600

# Retrieve screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate screen coordinates for window placement
screen_coordinate_x = (screen_width // 2) - (window_width // 2)
screen_coordinate_y = (screen_height // 2) - (window_height // 2)

# Set window geometry and title
root.geometry(f'{window_width}x{window_height}+{screen_coordinate_x}+{screen_coordinate_y}')
root.title('Expenses Tracker')

# Create a ttk Style instance
style = ttk.Style()

# Define color scheme
colors = {
    'primary_color': '#265073',
    'secondary_color': '#DDF2FD',
    'font_color': '#fff',
    'label_color': '#265073',
    'btn_color': '#2D9596',
}

# Configure root column weights and background color
root.columnconfigure(0, weight=8)
root.columnconfigure(1, weight=2)
root.configure(bg=colors['primary_color'])

# Create a frame for the title with specified background color
title_frame = Frame(root, bg=colors['primary_color'])
title_frame.grid(row=0, column=0, sticky='nesw')

# Create a label for the main title with specified font and colors
main_title = Label(title_frame, text='Expenses Tracker', font=(font_family, main_font_size), bg=colors['primary_color'], fg=colors['font_color'])
main_title.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)

# Create a frame for the search input with specified background color
search_input_place = Frame(root, bg=colors['primary_color'])
search_input_place.grid(row=1, column=0, sticky='nesw', padx=10, pady=10)

# Configure column weights for search_input_place
search_input_place.columnconfigure(0, weight=8)
search_input_place.columnconfigure(1, weight=1)

# Create a ttk Entry widget for search input with specified font
search_input = ttk.Entry(search_input_place, font=(font_family, main_font_size))
search_input.grid(row=0, column=0, sticky='nesw')

# Create a search button with specified properties
search_icon = PhotoImage(file='./assets/search_icon.png')
search_btn = Button(search_input_place, text='Search', relief='flat', bg=colors['btn_color'], fg=colors['font_color'], font=(font_family, 13))
search_btn.grid(row=0, column=1, sticky='nesw', padx=(10, 0))
search_btn.config(image=search_icon, compound=LEFT, width=60, padx=10)

# Create a frame for displaying expenses with specified background color, padding, and alignment
display_expenses_place = Frame(root, bg=colors['secondary_color'], padx=10, pady=10)
display_expenses_place.grid(row=2, column=0, sticky='nesw', padx=10, pady=10)
display_expenses_place.columnconfigure(0, weight=1)

# Create a label for displaying expenses count with specified font and colors
display_expenses_label = Label(display_expenses_place, text='All your expenses (10)', font=(font_family, 12), bg=colors['secondary_color'], fg=colors['label_color'])
display_expenses_label.grid(row=0, column=0, sticky='nw')

# Create a frame for status bar with expense labels and their properties
status_expenses_bar = Frame(display_expenses_place)
status_expenses_bar.grid(row=1, column=0, sticky='nesw', padx=0, pady=10)

expenses_status_labels  = ['Amount', 'Currency', 'Cateegory', 'Payment Method', 'Date']

# Loop through the expense status labels and create corresponding labels with specified properties
for i, text in enumerate(expenses_status_labels):
    status_expenses_bar.columnconfigure(i, weight=1)
    labels = Label(status_expenses_bar, text=text, font=(font_family, 12), borderwidth=2, relief='groove', padx=5, pady=5, bg=colors['btn_color'], fg=colors['font_color'])
    labels.grid(row=0, column=i, sticky='nesw')

# Create a frame for adding new expenses with specified background color, padding, and alignment
add_new_expenses_place = Frame(root,  bg=colors['secondary_color'], padx=10, pady=10)
add_new_expenses_place.grid(row=2, column=1, sticky='nesw', padx=10, pady=10)
add_new_expenses_place.columnconfigure(0, weight=1)

# Create a label for adding new expenses with specified font and colors
add_expenses_label = Label(add_new_expenses_place, text='Add a new expenses', font=(font_family, input_font_size),  bg=colors['secondary_color'], fg=colors['label_color'])
add_expenses_label.grid(row=0, column=0, sticky='nw')

# Create labels and input fields for different expense details with specified font and colors
amount_label = Label(add_new_expenses_place, text='Amount', font=(font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
amount_label.grid(row=1, column=0, sticky='nw', pady=(10, 0))
amount_input = ttk.Entry(add_new_expenses_place, font=(font_family, input_font_size))
amount_input.grid(row=2, column=0, sticky='nesw', pady=(0, 5))

currency_label = Label(add_new_expenses_place, text='Currency', font=(font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
currency_label.grid(row=3, column=0, sticky='nw', pady=(10, 0))
currency_optionos = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
selected_currency = StringVar()
currency_list = ttk.Combobox(add_new_expenses_place, textvariable=selected_currency, values=currency_optionos, font=(font_family, input_font_size))
currency_list.grid(row=4, column=0, sticky='nesw', pady=(0, 5))
# (Continuing from the previous code)

# Create labels and input fields for category, payment method, and date with specified font and colors
cateegory_label = Label(add_new_expenses_place, text='Category', font=(font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
cateegory_label.grid(row=5, column=0, sticky='nw', pady=(10, 0))
cateegory_optionos = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
selected_category = StringVar()
category_list = ttk.Combobox(add_new_expenses_place, textvariable=selected_category, values=cateegory_optionos, font=(font_family, input_font_size))
category_list.grid(row=6, column=0, sticky='nesw', pady=(0, 5))

payment_method_label = Label(add_new_expenses_place, text='Payment Method', font=(font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
payment_method_label.grid(row=7, column=0, sticky='nw', pady=(10, 0))
payment_method_options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
selected_payment_method = StringVar()
payment_method_list = ttk.Combobox(add_new_expenses_place, textvariable=selected_payment_method, values=payment_method_options, font=(font_family, input_font_size))
payment_method_list.grid(row=8, column=0, sticky='nesw', pady=(0, 5))

date_label = Label(add_new_expenses_place, text='Date', font=(font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
date_label.grid(row=9, column=0, sticky='nw', pady=(10, 0))
date_input = ttk.Entry(add_new_expenses_place, font=(font_family, input_font_size))
date_input.grid(row=10, column=0, sticky='nesw')

# Create a button to add expenses with specified properties
add_new_expenses_btn = Button(add_new_expenses_place, text='Add Expenses', relief='flat', bg=colors['btn_color'], fg=colors['font_color'], font=(font_family, 15))
add_new_expenses_btn.grid(row=11, column=0, sticky='nesw', pady=(25, 0))

# Run the Tkinter main loop
root.mainloop()

