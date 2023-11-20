import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()  # Prompt to choose a file to open
    if file_path:  # If a file is selected
        with open(file_path, 'r') as file:  # Open the file in read mode
            text_area.delete('1.0', tk.END)  # Clear any existing text in the text area
            text_area.insert(tk.END, file.read())  # Insert file content into the text area

def save_file():
    file_path = filedialog.asksaveasfilename(  # Prompt to choose a location and name to save the file
        defaultextension=".txt",  # Default extension for the file
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]  # Specify allowed file types
    )
    if file_path:  # If a file path is selected
        with open(file_path, 'w') as file:  # Open the file in write mode
            file.write(text_area.get('1.0', tk.END))  # Write the content of the text area into the file

window = tk.Tk()
window.title("AlmdrasaTextEditor")

frame = tk.Frame(window, bg="lightgray", padx=10, pady=10)  # Create a frame within the window with background color and padding
frame.pack(fill="both", expand=True)  # Place the frame in the window and allow it to expand

text_area = tk.Text(frame, bg="white", fg="black")  # Create a text area widget with white background and black text color
text_area.pack(fill="both", expand=True)  # Place the text area in the frame and allow it to expand

button_frame = tk.Frame(frame, bg="lightgray")  # Create another frame within the main frame for buttons with background color
button_frame.pack(side="left", fill="y")  # Place this frame to the left side of the main frame and let it fill vertically

open_button = tk.Button(button_frame, text="Open File", command=open_file, bg="skyblue", fg="white", width=15, height=2)  # Create a button to open a file with specific color and size
open_button.pack(fill="x", pady=5)  # Place the open button within its frame and let it fill horizontally

save_button = tk.Button(button_frame, text="Save File", command=save_file, bg="salmon", fg="white", width=15, height=2)  # Create a button to save a file with specific color and size
save_button.pack(fill="x", pady=5)  # Place the save button within its frame and let it fill horizontally



window.mainloop()
