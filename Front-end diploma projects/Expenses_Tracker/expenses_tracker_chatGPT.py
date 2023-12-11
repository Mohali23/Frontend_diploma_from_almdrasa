from tkinter import *
from tkinter import ttk, messagebox

import requests

class ExpenseManager:
    def __init__(self):
        self.expenses_list = []
        self.total_amount = 0.0
        self.font_family = 'Bahnschrift'
        self.main_font_size = 20
        self.input_font_size = 13
        self.create_gui()
        
    def convert_currency(self, from_currency, amount):

        to_currency = 'USD'

        # Construct the API URL with the provided parameters
        url = f"https://api.apilayer.com/fixer/convert?apikey={self.api_key}&from={from_currency}&to={to_currency}&amount={amount}"
        
        # Send a GET request to the API
        response = requests.get(url)
        
        # Check if the response status is successful (status code 200)
        if response.status_code == 200:
            # Convert the response to JSON format
            data = response.json()
            # Retrieve the converted amount from the response data
            converted_amount = round(data.get('result'), 1)
            
            # Get the current text in the label and extract the numerical value
            current_value = float(self.total_expenses_label.cget("text").split(": $")[1])
            
            # Add the newly converted amount to the current value
            total_amount = round(current_value + converted_amount, 1)
            
            # Update the label with the total amount in dollars
            self.total_expenses_label.config(text=f'Total amount in dollars: ${total_amount}')

    api_key = '8juraaxZMK8Vf8AsZMKJyKZ7LF5lpmD9'  # API key

    def add_expenses(self):
        # Extract values from input fields
        amount = self.amount_input.get()
        currency = self.currency_list.get()
        category = self.category_list.get()
        payment_method = self.payment_method_list.get()
        date = self.date_input.get()

        # Create a list to store the new expenses
        expenses_list = [amount, currency, category, payment_method, date]

        if amount == '' or currency =='' or category == '' or payment_method == '' or date == '':
            # Show an error message if any field is empty
            messagebox.showerror('Erorr', 'Please fill out all fields')
        else:
            # Insert the new expenses into the expenses table
            self.expenses_table.insert(parent='', index='end', text='', values=expenses_list)

            # Reset the fields after addition 
            self.reset_inputs()
            # Convert currency and display it accordingly
            self.convert_currency(currency, amount)


    def search_expenses(self):
        # Get the entered text for searching
        search_text = self.search_input.get().lower()
        found_rows = []
        # Search within the expenses table
        for row in self.expenses_table.get_children():
            values = self.expenses_table.item(row, 'values')
            # Check for text match in rows and select the matching item
            if search_text in [str(value).lower() for value in values]:
                found_rows.append(row)
        
        # Clear current selection
        self.expenses_table.selection_remove(*self.expenses_table.get_children())
        
        if found_rows:
            for row in found_rows:
                self.expenses_table.selection_add(row)
                self.expenses_table.focus(row)
        else:
            messagebox.showinfo("Not Found", "The search term was not found in the table.")


    def reset_inputs(self):
        # Clear the content of the 'amount_input' field
        self.amount_input.delete(0, 'end')
        # Reset the selected value in the 'currency_list' dropdown to empty
        self.currency_list.set('')
        # Reset the selected value in the 'category_list' dropdown to empty
        self.category_list.set('')
        # Reset the selected value in the 'payment_method_list' dropdown to empty
        self.payment_method_list.set('')
        # Clear the content of the 'date_input' field
        self.date_input.delete(0, 'end')

    def create_gui(self):
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
        self.title_frame = Frame(root, bg=colors['primary_color'])
        self.title_frame.grid(row=0, column=0, sticky='nesw')

        # Create a label for the main title with specified font and colors
        self.main_title = Label(self.title_frame, text='Expenses Tracker', font=(self.font_family, self.main_font_size), bg=colors['primary_color'], fg=colors['font_color'])
        self.main_title.grid(row=0, column=0, sticky='nesw', padx=10, pady=10)

        # Create a frame for the search input with specified background color
        self.search_input_place = Frame(root, bg=colors['primary_color'])
        self.search_input_place.grid(row=1, column=0, sticky='nesw', padx=10, pady=10)

        # Configure column weights for search_input_place
        self.search_input_place.columnconfigure(0, weight=8)
        self.search_input_place.columnconfigure(1, weight=1)

        # Create a ttk Entry widget for search input with specified font
        self.search_input = ttk.Entry(self.search_input_place, font=(self.font_family, self.main_font_size))
        self.search_input.grid(row=0, column=0, sticky='nesw')


        # Create a search button with specified properties
        self.search_icon = PhotoImage(file='./assets/search_icon.png')
        self.search_btn = Button(self.search_input_place, text='Search', relief='flat', bg=colors['btn_color'], fg=colors['font_color'], font=(self.font_family, 13), command=self.search_expenses)
        self.search_btn.grid(row=0, column=1, sticky='nesw', padx=(10, 0))
        self.search_btn.config(image=self.search_icon, compound=LEFT, width=60, padx=10)

        # Create a frame for displaying expenses with specified background color, padding, and alignment
        self.display_expenses_place = Frame(root, bg=colors['secondary_color'], padx=10, pady=10)
        self.display_expenses_place.grid(row=2, column=0, sticky='nesw', padx=10, pady=(10, 0))
        self.display_expenses_place.columnconfigure(0, weight=1)
        self.display_expenses_place.rowconfigure(1, weight=1)

        # Create a label for displaying expenses count with specified font and colors
        self.display_expenses_label = Label(self.display_expenses_place, text=f'All your expenses', font=(self.font_family, 12), bg=colors['secondary_color'], fg=colors['label_color'])
        self.display_expenses_label.grid(row=0, column=0, sticky='nw')

        # List of columns for the expenses table
        self.expenses_table = ('Amount', 'Currency', 'Category', 'Payment Method', 'Date')

        # Configure the style for the headings in the Treeview
        style.configure("Treeview.Heading", font=(self.font_family, 11), background=colors['btn_color'], foreground=colors['font_color'], relief='falt')

        # Map the background color for active headings in the Treeview
        style.map("Treeview.Heading", background=[('active', colors['btn_color'])])

        # Configure the general style for the Treeview
        style.configure("Treeview", font=(self.font_family, 11))

        # Create a Treeview widget for displaying expenses
        self.expenses_table = ttk.Treeview(self.display_expenses_place, columns=(self.expenses_table))
        self.expenses_table.grid(row=1, column=0, sticky='nesw', padx=0, pady=(10, 0))

        # Hide the first column ('#0') in the expenses_table
        self.expenses_table.column('#0', width=0, stretch=NO)
        self.expenses_table.heading('#0', text='', anchor='nw')

        # Loop through each column in expenses_table's 'columns'
        for col in self.expenses_table['columns']:
            # Set column configurations: anchor, width
            self.expenses_table.column(col, anchor='nw', width=100)
            # Set heading configurations: text, anchor
            self.expenses_table.heading(col, text=col, anchor='nw')


        # Create a frame for displaying the total expenses bar
        self.total_expenses_bar = Frame(self.display_expenses_place, bg=colors['secondary_color'])
        self.total_expenses_bar.grid(row=2, column=0, sticky='nesw')

        # Configure the first column of total_expenses_bar to expand proportionally
        self.total_expenses_bar.columnconfigure(0, weight=1)

        # Create a label for displaying the total amount of expenses in dollars
        self.total_expenses_label = Label(self.total_expenses_bar, text=f'Total amount in dollars: ${0}', font=(self.font_family, 12), anchor='nw', borderwidth=2, relief='groove', padx=5, pady=5, bg=colors['btn_color'], fg=colors['font_color'])
        self.total_expenses_label.grid(row=0, column=0, sticky='nesw')


        # Create a frame for adding new expenses with specified background color, padding, and alignment
        self.add_new_expenses_place = Frame(root,  bg=colors['secondary_color'], padx=10, pady=10)
        self.add_new_expenses_place.grid(row=2, column=1, sticky='nesw', padx=10, pady=10)
        self.add_new_expenses_place.columnconfigure(0, weight=1)

        # Create a label for adding new expenses with specified font and colors
        self.add_expenses_label = Label(self.add_new_expenses_place, text='Add a new expenses', font=(self.font_family, self.input_font_size),  bg=colors['secondary_color'], fg=colors['label_color'])
        self.add_expenses_label.grid(row=0, column=0, sticky='nw')

        # Create labels and input fields for different expense details with specified font and colors
        # Create a label for 'Amount'
        self.amount_label = Label(self.add_new_expenses_place, text='Amount', font=(self.font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
        self.amount_label.grid(row=1, column=0, sticky='nw', pady=(10, 0))

        # Create an entry field for entering the amount
        self.amount_input = ttk.Entry(self.add_new_expenses_place, font=(self.font_family, self.input_font_size))
        self.amount_input.grid(row=2, column=0, sticky='nesw', pady=(0, 5))

        # Create a label for 'Currency'
        self.currency_label = Label(self.add_new_expenses_place, text='Currency', font=(self.font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
        self.currency_label.grid(row=3, column=0, sticky='nw', pady=(10, 0))

        # List of currency options
        self.currency_options = ['EGP', 'GBP', 'EUR']

        # Define a variable to store the selected currency
        self.selected_currency = StringVar()

        # Create a combobox for selecting the currency
        self.currency_list = ttk.Combobox(self.add_new_expenses_place, textvariable=self.selected_currency, values=self.currency_options, font=(self.font_family, self.input_font_size))
        self.currency_list.grid(row=4, column=0, sticky='nesw', pady=(0, 5))

        # Create labels and input fields for category, payment method, and date with specified font and colors
        # Create a label for 'Category'
        self.category_label = Label(self.add_new_expenses_place, text='Category', font=(self.font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
        self.category_label.grid(row=5, column=0, sticky='nw', pady=(10, 0))

        # List of category options
        self.category_options = ['Life expenses', 'Electricity', 'Gas', 'Rental', 'Grocery', 'Savings', 'Education', 'Charity']

        # Define a variable to store the selected category
        self.selected_category = StringVar()

        # Create a combobox for selecting the category
        self.category_list = ttk.Combobox(self.add_new_expenses_place, textvariable=self.selected_category, values=self.category_options, font=(self.font_family, self.input_font_size))
        self.category_list.grid(row=6, column=0, sticky='nesw', pady=(0, 5))

        # Create a label for 'Payment Method'
        self.payment_method_label = Label(self.add_new_expenses_place, text='Payment Method', font=(self.font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
        self.payment_method_label.grid(row=7, column=0, sticky='nw', pady=(10, 0))

        # List of payment method options
        self.payment_method_options = ['Cash', 'Credit Card', 'PayPal']

        # Define a variable to store the selected payment method
        self.selected_payment_method = StringVar()

        # Create a combobox for selecting the payment method
        self.payment_method_list = ttk.Combobox(self.add_new_expenses_place, textvariable=self.selected_payment_method, values=self.payment_method_options, font=(self.font_family, self.input_font_size))
        self.payment_method_list.grid(row=8, column=0, sticky='nesw', pady=(0, 5))

        # Create a label for 'Date'
        self.date_label = Label(self.add_new_expenses_place, text='Date', font=(self.font_family, 10), bg=colors['secondary_color'], fg=colors['label_color'])
        self.date_label.grid(row=9, column=0, sticky='nw', pady=(10, 0))

        # Create an entry field for entering the date
        self.date_input = ttk.Entry(self.add_new_expenses_place, font=(self.font_family, self.input_font_size))
        self.date_input.grid(row=10, column=0, sticky='nesw')

        # Create a button to add expenses with specified properties
        self.add_new_expenses_btn = Button(
            self.add_new_expenses_place, 
            text='Add Expenses', 
            relief='flat', 
            bg=colors['btn_color'], 
            fg=colors['font_color'], 
            font=(self.font_family, 15), 
            command=self.add_expenses
        )
        self.add_new_expenses_btn.grid(row=11, column=0, sticky='nesw', pady=(25, 0))


        root.mainloop()

ui_manager = ExpenseManager()


