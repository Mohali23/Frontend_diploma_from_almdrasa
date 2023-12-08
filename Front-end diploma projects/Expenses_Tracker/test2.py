# # import tkinter as tk
# # from tkinter import ttk

# # root = tk.Tk()
# # root.title("Listbox using ttk.Treeview")

# # # Create a Treeview widget
# # listbox = ttk.Treeview(root)

# # # Add columns (if needed)
# # listbox['columns'] = ("column1", "column2")  # Example columns

# # # Define columns heading
# # listbox.heading("#0", text="Items")  # Main column
# # listbox.heading("column1", text="Column 1")  # Additional column(s), if any
# # listbox.heading("column2", text="Column 2")  # Additional column(s), if any

# # # Insert items into the list
# # listbox.insert("", "end", text="Item 1", values=("Value 1", "Value 2"))  # Inserting items with values
# # listbox.insert("", "end", text="Item 2", values=("Value 3", "Value 4"))  # Inserting items with values
# # # ...

# # listbox.pack()

# # root.mainloop()


# # status_expenses_bar = ttk.Treeview(display_expenses_place, columns=("column1", "column2", ...))  # قم بتحديد الأعمدة هنا

# # status_expenses_bar = ttk.Treeview(display_expenses_place)
# # status_expenses_bar['columns'] = ("column1", "column2", ...)  # قم بتحديد الأعمدة هنا بعد إنشاء `ttk.Treeview`


# # status_expenses_bar = ttk.Treeview(display_expenses_place)
# # status_expenses_bar.grid(row=2, column=0, sticky='nesw')

# # status_expenses_bar['columns'] = expenses_status_labels  # تحديد الأعمدة
# # for i, text in enumerate(expenses_status_labels):
# #     status_expenses_bar.heading('#' + str(i), text=text)  # تعيين رأس العمود













# # status_expenses_bar = ttk.Treeview(display_expenses_place)
# # status_expenses_bar.grid(row=2, column=0, sticky='nw')

# # expenses_status_labels  = ['Amount', 'Currency', 'Category', 'Payment Method']
# # status_expenses_bar['columns'] = expenses_status_labels
# # for i, text in enumerate(expenses_status_labels):
# #     status_expenses_bar.heading('#' + str(i), text=text)




# # import tkinter as tk
# # from tkinter import ttk

# # root = tk.Tk()
# # root.title("Resizing Treeview Example")

# # # إنشاء نمط جديد لـ `Treeview`
# # style = ttk.Style()
# # style.configure("mystyle.Treeview", rowheight=25)  # قم بتحديد ارتفاع الصفوف هنا

# # # إنشاء `Treeview` باستخدام النمط المحدد
# # status_expenses_bar = ttk.Treeview(root, style="mystyle.Treeview", columns=("column1", "column2", "column3"), show="headings")
# # status_expenses_bar.grid(row=2, column=0, sticky='nw')

# # # قم بتعيين رؤوس الأعمدة وأي عمليات أخرى لـ `ttk.Treeview` هنا

# # root.mainloop()


# # import tkinter as tk
# # from tkinter import ttk

# # root = tk.Tk()
# # root.title("Column Width in Treeview")

# # # إنشاء `Treeview`
# # status_expenses_bar = ttk.Treeview(root, columns=("column1", "column2", "column3"), show="headings")
# # status_expenses_bar.grid(row=2, column=0, sticky='nw')

# # # تعيين العنوان (heading) والعرض الأدنى لكل عمود
# # status_expenses_bar.heading("column1", text="Column 1", anchor=tk.CENTER)
# # status_expenses_bar.column("column1", minwidth=100, anchor=tk.CENTER)

# # status_expenses_bar.heading("column2", text="Column 2", anchor=tk.CENTER)
# # status_expenses_bar.column("column2", minwidth=150, anchor=tk.CENTER)

# # status_expenses_bar.heading("column3", text="Column 3", anchor=tk.CENTER)
# # status_expenses_bar.column("column3", minwidth=200, anchor=tk.CENTER)

# # root.mainloop()


# # import tkinter as tk
# # from tkinter import ttk

# # root = tk.Tk()
# # root.title("Dropdown List Example")

# # # إنشاء `Combobox`
# # options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']
# # selected_option = tk.StringVar()  # لتخزين القيمة المحددة
# # combobox = ttk.Combobox(root, textvariable=selected_option, values=options)
# # combobox.pack()

# # root.mainloop()


# # import tkinter as tk
# # from tkcalendar import Calendar

# # root = tk.Tk()
# # root.title("Calendar Example")

# # # إنشاء وعرض التقويم
# # cal = Calendar(root, selectmode='day', year=2023, month=12, day=7)
# # cal.pack()

# # root.mainloop()
# # Import the required libraries

# # from tkinter import ttk
# # from tkinter import Tk

# # root = Tk()
# # style = ttk.Style()
# # button_1 = ttk.Button(root, text='click me')
# # style.theme_use('alt')
# # style.configure('TButton', font=('American typewriter', 14), background='#ff0000', foreground='white')
# # style.map('TButton', background=[('active', '#ff0000')])
# # button_1.pack()

# # root.mainloop()


# from tkinter import ttk
# import tkinter as tk
# root = tk.Tk()

# style = ttk.Style()
# style.configure('Custom.TLabel', background='red')

# slider = ttk.Button(root, text="Hello World", style='Custom.TLabel')
# slider.pack(pady=20)

# root.mainloop()
