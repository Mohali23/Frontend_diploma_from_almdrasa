import tkinter as tk  # Import the tkinter module for GUI

from tkinter import filedialog  # Import filedialog submodule from tkinter

# Function to open a file and display its content in the text area
def open_file():
    file_path = filedialog.askopenfilename()  # Prompt to choose a file to open
    if file_path:  # If a file is selected
        with open(file_path, 'r') as file:  # Open the file in read mode
            text_area.delete(1.0, tk.END)  # Clear any existing text in the text area
            text_area.insert(1.0, file.read())  # Insert file content into the text area

# Function to save the file
def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", 
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )  # Prompt to choose a location and name to save the file, specifying allowed file types
    
    if file_path:  # If a file path is selected
        with open(file_path, 'w') as file:  # Open the file in write mode
            file.write(text_area.get(1.0, tk.END))  # Write the content of the text area into the file

window = tk.Tk()  # Create the main window
window.title("AlmdrasaTextEditor")  # Set the title of the window

window.columnconfigure(0, weight=1)  # Configure column 0 to expand
window.rowconfigure(0, weight=1)  # Configure row 0 to expand

frame = tk.Frame(window)  # Create a frame within the window
frame.grid(row=0, column=0, sticky="nsew")  # Place the frame in the window, allowing it to expand

text_area = tk.Text(frame)  # Create a text area widget
text_area.grid(row=0, column=1, sticky="nsew")  # Place the text area in the frame, allowing it to expand

button_frame = tk.Frame(frame)  # Create another frame within the main frame for buttons
button_frame.grid(row=0, column=0, sticky="n")  # Place this frame to the left side of the main frame

open_button = tk.Button(button_frame, text="Open File", command=open_file)  # Create a button to open a file
open_button.grid(row=0, column=0, sticky="ew")  # Place the open button within its frame, allowing it to expand in the x-direction

save_button = tk.Button(button_frame, text="Save File", command=save_file)  # Create a button to save a file
save_button.grid(row=1, column=0, sticky="ew")  # Place the save button within its frame, allowing it to expand in the x-direction

window.mainloop()  # Start the GUI event loop
