
# Import necessary libraries
import requests  # Importing requests module to make HTTP requests
from tkinter import *  # Importing all classes from tkinter module
from tkinter import ttk  # Importing ttk class from tkinter module
from tkinter import messagebox


def convert_currency(from_currency, amount):
    
    to_currency = 'USD'

    # Construct the API URL with the provided parameters
    url = f"https://api.apilayer.com/fixer/convert?apikey={api_key}&from={from_currency}&to={to_currency}&amount={amount}"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the response status is successful (status code 200)
    if response.status_code == 200:
        # Convert the response to JSON format
        data = response.json()
        # Retrieve the converted amount from the response data
        converted_amount = round(data.get('result'), 1)
        
        # Get the current text in the label and extract the numerical value
        current_value = float(total_expenses_label.cget("text").split(": $")[1])
        
        # Add the newly converted amount to the current value
        total_amount = round(current_value + converted_amount, 1)
        
        # Update the label with the total amount in dollars
        total_expenses_label.config(text=f'Total amount in dollars: ${total_amount}')

api_key = '8juraaxZMK8Vf8AsZMKJyKZ7LF5lpmD9'  # API key


def add_expenses():
  # Extract values from input fields
  amount = amount_input.get()
  currency = currency_list.get()
  category = category_list.get()
  payment_method = payment_method_list.get()
  date = date_input.get()

  # Create a list to store the new expenses
  expenses_list = [amount, currency, category, payment_method, date]

  if amount == '' or currency =='' or category == '' or payment_method == '' or date == '':
    # Show an error message if any field is empty
    messagebox.showerror('Erorr', 'Please fill out all fields')
  else:
    # Insert the new expenses into the expenses table
    expenses_table.insert(parent='', index='end', text='', values=expenses_list)

    # Reset the fields after addition 
    reset_inputs()
    # Convert currency and display it accordingly
    convert_currency(currency, amount)


def search_expenses():
    # Get the entered text for searching
    search_text = search_input.get().lower()
    found_rows = []
    # Search within the expenses table
    for row in expenses_table.get_children():
        values = expenses_table.item(row, 'values')
        # Check for text match in rows and select the matching item
        if search_text in [str(value).lower() for value in values]:
            found_rows.append(row)
    
    # Clear current selection
    expenses_table.selection_remove(*expenses_table.get_children())
    
    if found_rows:
        for row in found_rows:
            expenses_table.selection_add(row)
            expenses_table.focus(row)
    else:
        messagebox.showinfo("Not Found", "The search term was not found in the table.")


def reset_inputs():
  # Clear the content of the 'amount_input' field
  amount_input.delete(0, 'end')
  # Reset the selected value in the 'currency_list' dropdown to empty
  currency_list.set('')
  # Reset the selected value in the 'category_list' dropdown to empty
  category_list.set('')
  # Reset the selected value in the 'payment_method_list' dropdown to empty
  payment_method_list.set('')
  # Clear the content of the 'date_input' field
  date_input.delete(0, 'end')


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
style.theme_use("clam")

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
search_btn = Button(search_input_place, text='Search', relief='flat', bg=colors['btn_color'], fg=colors['font_color'], font=(font_family, 13), command=search_expenses)
search_btn.grid(row=0, column=1, sticky='nesw', padx=(10, 0))
search_btn.config(image=search_icon, compound=LEFT, width=60, padx=10)

# Create a frame for displaying expenses with specified background color, padding, and alignment
display_expenses_place = Frame(root, bg=colors['secondary_color'], padx=10, pady=10)
display_expenses_place.grid(row=2, column=0, sticky='nesw', padx=10, pady=(10, 0))
display_expenses_place.columnconfigure(0, weight=1)
display_expenses_place.rowconfigure(1, weight=1)

# Create a label for displaying expenses count with specified font and colors
display_expenses_label = Label(display_expenses_place, text=f'All your expenses', font=(font_family, 12), bg=colors['secondary_color'], fg=colors['label_color'])
display_expenses_label.grid(row=0, column=0, sticky='nw')

# List of columns for the expenses table
expenses_table = ('Amount', 'Currency', 'Category', 'Payment Method', 'Date')

# Configure the style for the headings in the Treeview
style.configure("Treeview.Heading", font=(font_family, 11), background=colors['btn_color'], foreground=colors['font_color'], relief='falt')

# Map the background color for active headings in the Treeview
style.map("Treeview.Heading", background=[('active', colors['btn_color'])])

# Configure the general style for the Treeview
style.configure("Treeview", font=(font_family, 11))

# Create a Treeview widget for displaying expenses
expenses_table = ttk.Treeview(display_expenses_place, columns=(expenses_table))
expenses_table.grid(row=1, column=0, sticky='nesw', padx=0, pady=(10, 0))

# Hide the first column ('#0') in the expenses_table
expenses_table.column('#0', width=0, stretch=NO)
expenses_table.heading('#0', text='', anchor='nw')

# Loop through each column in expenses_table's 'columns'
for col in expenses_table['columns']:
    # Set column configurations: anchor, width
    expenses_table.column(col, anchor='nw', width=100)
    # Set heading configurations: text, anchor
    expenses_table.heading(col, text=col, anchor='nw')


# Create a frame for displaying the total expenses bar
total_expenses_bar = Frame(display_expenses_place, bg=colors['secondary_color'])
total_expenses_bar.grid(row=2, column=0, sticky='nesw')

# Configure the first column of total_expenses_bar to expand proportionally
total_expenses_bar.columnconfigure(0, weight=1)

# Create a label for displaying the total amount of expenses in dollars
total_expenses_label = Label(total_expenses_bar, text=f'Total amount in dollars: ${0}', font=(font_family, 12), anchor='nw', borderwidth=2, relief='groove', padx=5, pady=5, bg=colors['btn_color'], fg=colors['font_color'])
total_expenses_label.grid(row=0, column=0, sticky='nesw')


# Create a frame for adding new expenses with specified background color, padding, and alignment
add_new_expenses_place = Frame(root,  bg=colors['secondary_color'], padx=10, pady=10)
add_new_expenses_place.grid(row=2, column=1, sticky='nesw', padx=10, pady=10)
add_new_expenses_place.columnconfigure(0, weight=1)

# Create a label for adding new expenses with specified font and colors
add_expenses_label = Label(add_new_expenses_place, text='Add a new expenses', font=(font_family, input_font_size),  bg=colors['secondary_color'], fg=colors['label_color'])
add_expenses_label.grid(row=0, column=0, sticky='nw')

# Create labels and input fields for different expense details with specified font and colors
# Create a label for 'Amount'
amount_label = Label(add_new_expenses_place, text='Amount', font=(font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
amount_label.grid(row=1, column=0, sticky='nw', pady=(10, 0))

# Create an entry field for entering the amount
amount_input = ttk.Entry(add_new_expenses_place, font=(font_family, input_font_size))
amount_input.grid(row=2, column=0, sticky='nesw', pady=(0, 5))

# Create a label for 'Currency'
currency_label = Label(add_new_expenses_place, text='Currency', font=(font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
currency_label.grid(row=3, column=0, sticky='nw', pady=(10, 0))

# List of currency options
currency_options = ['EGP', 'GBP', 'EUR']

# Define a variable to store the selected currency
selected_currency = StringVar()

# Create a combobox for selecting the currency
currency_list = ttk.Combobox(add_new_expenses_place, textvariable=selected_currency, values=currency_options, font=(font_family, input_font_size))
currency_list.grid(row=4, column=0, sticky='nesw', pady=(0, 5))

# Create labels and input fields for category, payment method, and date with specified font and colors
# Create a label for 'Category'
category_label = Label(add_new_expenses_place, text='Category', font=(font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
category_label.grid(row=5, column=0, sticky='nw', pady=(10, 0))

# List of category options
category_options = ['Life expenses', 'Electricity', 'Gas', 'Rental', 'Grocery', 'Savings', 'Education', 'Charity']

# Define a variable to store the selected category
selected_category = StringVar()

# Create a combobox for selecting the category
category_list = ttk.Combobox(add_new_expenses_place, textvariable=selected_category, values=category_options, font=(font_family, input_font_size))
category_list.grid(row=6, column=0, sticky='nesw', pady=(0, 5))

# Create a label for 'Payment Method'
payment_method_label = Label(add_new_expenses_place, text='Payment Method', font=(font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
payment_method_label.grid(row=7, column=0, sticky='nw', pady=(10, 0))

# List of payment method options
payment_method_options = ['Cash', 'Credit Card', 'PayPal']

# Define a variable to store the selected payment method
selected_payment_method = StringVar()

# Create a combobox for selecting the payment method
payment_method_list = ttk.Combobox(add_new_expenses_place, textvariable=selected_payment_method, values=payment_method_options, font=(font_family, input_font_size))
payment_method_list.grid(row=8, column=0, sticky='nesw', pady=(0, 5))

# Create a label for 'Date'
date_label = Label(add_new_expenses_place, text='Date', font=(font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
date_label.grid(row=9, column=0, sticky='nw', pady=(10, 0))

# Create an entry field for entering the date
date_input = ttk.Entry(add_new_expenses_place, font=(font_family, input_font_size))
date_input.grid(row=10, column=0, sticky='nesw')

# Create a button to add expenses with specified properties
add_new_expenses_btn = Button(
    add_new_expenses_place, 
    text='Add Expenses', 
    relief='flat', 
    bg=colors['btn_color'], 
    fg=colors['font_color'], 
    font=(font_family, 15), 
    command=add_expenses
  )
add_new_expenses_btn.grid(row=11, column=0, sticky='nesw', pady=(25, 0))

# Run the Tkinter main loop
root.mainloop()

