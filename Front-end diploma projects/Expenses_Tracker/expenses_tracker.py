
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
        # Print the converted amount with currencies
        # total = sum(int(expenses_table.item(item, 'values')[0]) for item in expenses_table.get_children())
        total =+ converted_amount

        total_expenses_label.config(text=f'Total amount in dollars: ${total}')
    else:
        # If the request fails, print an error message
        print("Failed to convert. Please try again later.")


api_key = '8juraaxZMK8Vf8AsZMKJyKZ7LF5lpmD9'  # API key



def add_expenses():
  amount = amount_input.get()
  currency = currency_list.get()
  category = category_list.get()
  payment_method = payment_method_list.get()
  date = date_input.get()

  expenses_list = [amount, currency, category, payment_method, date]
  expenses_table.insert(parent='', index='end', text='', values=expenses_list)

  reset_inputs()
  convert_currency(currency, amount)

def search_expenses():
  search_text = search_input.get().lower()
  found = False
  for row in expenses_table.get_children():
    values = expenses_table.item(row, 'values')
    if search_text in [str(value).lower() for value in values]:
      expenses_table.selection_set(row)
      expenses_table.focus(row)
      expenses_table.selection()
      found = True
    else:
      expenses_table.selection_remove(row)

  if not found:
    messagebox.showinfo("Not Found", "The search term was not found in the table.")

def clear_search(event=None):  # استخدام event=None لضمان أنه يمكن استدعاء الدالة بشكل مستقل أيضًا
    search_input.delete(0, END)  # مسح حقل البحث
    for row in expenses_table.get_children():
        expenses_table.reattach(row, '', len(expenses_table.get_children()))  # إعادة عرض الصف

def reset_inputs():
  amount_input.delete(0, 'end')
  currency_list.set('')
  category_list.set('')
  payment_method_list.set('')
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
search_input.bind("<FocusOut>", clear_search)


# Create a search button with specified properties
search_icon = PhotoImage(file='./assets/search_icon.png')
search_btn = Button(search_input_place, text='Search', relief='flat', bg=colors['btn_color'], fg=colors['font_color'], font=(font_family, 13), command=search_expenses)
search_btn.grid(row=0, column=1, sticky='nesw', padx=(10, 0))
search_btn.config(image=search_icon, compound=LEFT, width=60, padx=10)

# Create a frame for displaying expenses with specified background color, padding, and alignment
display_expenses_place = Frame(root, bg=colors['secondary_color'], padx=10, pady=10)
display_expenses_place.grid(row=2, column=0, sticky='nesw', padx=10, pady=(10, 0))
display_expenses_place.columnconfigure(0, weight=1)

# Create a label for displaying expenses count with specified font and colors
display_expenses_label = Label(display_expenses_place, text=f'All your expenses', font=(font_family, 12), bg=colors['secondary_color'], fg=colors['label_color'])
display_expenses_label.grid(row=0, column=0, sticky='nw')


##########

expenses_table = ('Amount', 'Currency', 'Cateegory', 'Payment Method', 'Date')
style.configure("Treeview.Heading", font=(font_family, 11), background=colors['btn_color'], foreground=colors['font_color'], relief='falt')
style.map("Treeview.Heading", background=[('active', colors['btn_color'])])
style.configure("Treeview", font=(font_family, 11))

expenses_table = ttk.Treeview(display_expenses_place, columns=(expenses_table))
expenses_table.grid(row=1, column=0, sticky='nesw', padx=0, pady=(10, 0))


expenses_table.column('#0', width=0, stretch=NO)
expenses_table.heading('#0', text='', anchor='nw')
for col in expenses_table['columns']:
  expenses_table.column(col, anchor='nw', width=100)
  expenses_table.heading(col, text=col, anchor='nw')


##########

total_expenses_bar = Frame(display_expenses_place, bg=colors['secondary_color'])
total_expenses_bar.grid(row=2, column=0, sticky='nesw')
total_expenses_bar.columnconfigure(0, weight=1)


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
amount_label = Label(add_new_expenses_place, text='Amount', font=(font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
amount_label.grid(row=1, column=0, sticky='nw', pady=(10, 0))
amount_input = ttk.Entry(add_new_expenses_place, font=(font_family, input_font_size))
amount_input.grid(row=2, column=0, sticky='nesw', pady=(0, 5))

currency_label = Label(add_new_expenses_place, text='Currency', font=(font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
currency_label.grid(row=3, column=0, sticky='nw', pady=(10, 0))
currency_optionos = ['EGP', 'USD', 'GBP', 'EUR']
selected_currency = StringVar()
currency_list = ttk.Combobox(add_new_expenses_place, textvariable=selected_currency, values=currency_optionos, font=(font_family, input_font_size))
currency_list.grid(row=4, column=0, sticky='nesw', pady=(0, 5))

# Create labels and input fields for category, payment method, and date with specified font and colors
cateegory_label = Label(add_new_expenses_place, text='Category', font=(font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
cateegory_label.grid(row=5, column=0, sticky='nw', pady=(10, 0))
cateegory_optionos = ['Food', 'Rent', 'Transportation', 'Utilities', 'Entertainment']
selected_category = StringVar()
category_list = ttk.Combobox(add_new_expenses_place, textvariable=selected_category, values=cateegory_optionos, font=(font_family, input_font_size))
category_list.grid(row=6, column=0, sticky='nesw', pady=(0, 5))

payment_method_label = Label(add_new_expenses_place, text='Payment Method', font=(font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
payment_method_label.grid(row=7, column=0, sticky='nw', pady=(10, 0))
payment_method_options = ['Cash', 'Credit Card', 'Debit Card', 'Bank Transfer', 'PayPal']
selected_payment_method = StringVar()
payment_method_list = ttk.Combobox(add_new_expenses_place, textvariable=selected_payment_method, values=payment_method_options, font=(font_family, input_font_size))
payment_method_list.grid(row=8, column=0, sticky='nesw', pady=(0, 5))

date_label = Label(add_new_expenses_place, text='Date', font=(font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
date_label.grid(row=9, column=0, sticky='nw', pady=(10, 0))
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


# add_new_expenses_btn = Button(
#     add_new_expenses_place, 
#     text='Add Expenses', 
#     relief='flat', 
#     bg=colors['btn_color'], 
#     fg=colors['font_color'], 
#     font=(font_family, 15), 
#     command=lambda api_key=api_key, 
#     date_input=date_input, 
#     search_input=search_input, 
#     amount_input=amount_input: 
#     convert_currency(api_key, date_input, search_input, amount_input)
#   )

# # Create a frame for status bar with expense labels and their properties
# status_expenses_bar = Frame(display_expenses_place)
# status_expenses_bar.grid(row=1, column=0, sticky='nesw', padx=0, pady=(10, 0))

# expenses_status_labels  = ['Amount', 'Currency', 'Cateegory', 'Payment Method', 'Date']

# # Loop through the expense status labels and create corresponding labels with specified properties
# for i, text in enumerate(expenses_status_labels):
#     status_expenses_bar.columnconfigure(i, weight=1)
#     labels = Label(status_expenses_bar, text=text, font=(font_family, 12), borderwidth=2, relief='groove', padx=5, pady=5, bg=colors['btn_color'], fg=colors['font_color'])
#     labels.grid(row=0, column=i, sticky='nesw')


# #****

# # Create a frame for status bar with expense labels and their properties
# expenses_item = Frame(display_expenses_place)
# expenses_item.grid(row=2, column=0, sticky='nesw')

# expenses_status_item  = ['300', 'EGP', 'Rant', 'CashCashCashCashCashCashCashs', '10-12-2023']

# # Loop through the expense status labels and create corresponding labels with specified properties
# for i, text in enumerate(expenses_status_item):
#     expenses_item.columnconfigure(i, weight=1)
#     labels = Label(expenses_item, text=text, font=(font_family, 12), borderwidth=2, relief='groove', padx=5, pady=5, bg='#fff', fg=colors['label_color'])
#     labels.grid(row=0, column=i, sticky='nesw')

# #***