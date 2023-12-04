import requests
import tkinter as tk










# Create Tkinter window
root = tk.Tk()

# Window size and title
window_width = 600
window_height = 600

# Retrieve screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate screen coordinates for window placement
screen_coordinate_x = (screen_width // 2) - (window_width // 2)
screen_coordinate_y = (screen_height // 2) - (window_height // 2)

root.geometry(f'{window_width}x{window_height}+{screen_coordinate_x}+{screen_coordinate_y}')
root.title('Expenses Tracker')


# Run the Tkinter main loop
root.mainloop()
