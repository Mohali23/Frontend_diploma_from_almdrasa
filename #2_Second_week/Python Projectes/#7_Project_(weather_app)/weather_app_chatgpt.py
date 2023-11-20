import requests  # Importing the requests library for making HTTP requests
import tkinter as tk  # Importing the Tkinter library for creating the graphical user interface

# Function to fetch weather data using the API
def fetch_weather_data(location):
    api_key = 'e4fd85a8ac1727867a52c40a74c61505'  # API key for OpenWeatherMap
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(base_url)  # Sending a GET request to fetch data from the API
    return response.json() if response.status_code == 200 else None  # Converting the retrieved data to JSON

# Function to display weather data on the UI
def display_weather_data(weather_data):
    if weather_data:
        # Displaying the received data in UI elements
        temp_label.config(text=f'Temperature: {weather_data["main"]["temp"]}°C')
        humidity_label.config(text=f'Humidity: {weather_data["main"]["humidity"]}%')
        wind_speed_label.config(text=f'Wind Speed: {weather_data["wind"]["speed"]}km/h')
        pressure_label.config(text=f'Pressure: {weather_data["main"]["pressure"]}hPa')
        precipitation_label.config(text=f'Precipitation: N/A')
    else:
        error_message.config(text='Please enter the correct location')
        reset_labels()

# Function for searching weather data using the user-entered location
def search():
    location = search_input.get()
    if not location:
        error_message.config(text='Please fill the input field')
        return
    
    weather_data = fetch_weather_data(location)  # Fetching weather data using the above function
    display_weather_data(weather_data)  # Displaying weather data using the above function

# Function to clear error message
def clear_error_message(event=None):
    error_message.config(text='')

# Function to reset text labels to default values
def reset_labels():
    temp_label.config(text='Temperature: 0')
    humidity_label.config(text='Humidity: 0')
    wind_speed_label.config(text='Wind Speed: 0')
    pressure_label.config(text='Pressure: 0')
    precipitation_label.config(text='Precipitation: 0')

# Defining the fonts and sizes used for text labels
font_family = 'Arial'
font_size = 14

# Creating a Tkinter window for the user interface
window = tk.Tk()
window.title('Welcome to weather forecast app from Almdrasa')  # Setting the window title
window.geometry("450x400")  # Defining the window size

window.bind('<Button-1>', clear_error_message)  # Binding left mouse button click event to clear error message

window.columnconfigure(0, weight=1)  # Configuring column and row distribution
window.rowconfigure(0, weight=1)

frame = tk.Frame(window)  # Creating a frame inside the window
frame.grid(row=0, column=0, sticky='nsew')  # Defining the frame layout within the window
frame.columnconfigure(0, weight=7)  # Configuring column distribution inside the frame
frame.columnconfigure(1, weight=3)

label = tk.Label(frame, text="Enter the location", font=(font_family, font_size))  # Creating a label for the UI
label.grid(row=0, column=0, sticky='nw', padx=5, pady=5)  # Defining the label layout inside the frame

btn_search = tk.Button(frame, text='Search', command=search)  # Creating a search button
btn_search.grid(row=1, column=1, sticky='ew', padx=5, pady=5)  # Defining the search button layout inside the frame

search_input = tk.Entry(frame)  # Creating a text entry for entering the location
search_input.grid(row=1, column=0, sticky='ew', padx=5, pady=5)  # Defining the text entry layout inside the frame
search_input.bind('<FocusIn>', clear_error_message)  # Binding the focus in event of the entry to clear error message
search_input.bind('<Return>', lambda event: search())

temp_label = tk.Label(frame, text='Temperature: 0', font=(font_family, font_size))  # Creating a label for temperature
temp_label.grid(row=2, column=0, sticky='nw', padx=5, pady=5)  # Defining the temperature label layout inside the frame

humidity_label = tk.Label(frame, text='Humidity: 0', font=(font_family, font_size))  # Creating a label for humidity
humidity_label.grid(row=3, column=0, sticky='nw', padx=5, pady=5)  # Defining the humidity label layout inside the frame

wind_speed_label = tk.Label(frame, text='Wind Speed: 0', font=(font_family, font_size))  # Creating a label for wind speed
wind_speed_label.grid(row=4, column=0, sticky='nw', padx=5, pady=5)  # Defining the wind speed label layout inside the frame

pressure_label = tk.Label(frame, text='Pressure: 0', font=(font_family, font_size))  # Creating a label for pressure
pressure_label.grid(row=5, column=0, sticky='nw', padx=5, pady=5)  # Defining the pressure label layout inside the frame

precipitation_label = tk.Label(frame, text='Precipitation: 0', font=(font_family, font_size))  # Creating a label for precipitation
precipitation_label.grid(row=6, column=0, sticky='nw', padx=5, pady=5)  # Defining the precipitation label layout inside the frame

error_message = tk.Label(frame, text='', font=(font_family, font_size), fg="red")  # Creating a label for error message
error_message.grid(row=7, column=0, sticky='nw', padx=5, pady=5)  # Defining the error message label layout inside the frame

window.mainloop()  # Running the main event loop to display the user interface
