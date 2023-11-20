import requests  # Importing the requests library to handle HTTP requests
import tkinter as tk  # Importing the tkinter library for creating the graphical user interface

# Function to perform weather data search
def search(e=None):
    # Getting the user-input location
    location = search_input.get()
    
    # Constructing the API URL based on the location entered by the user
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={'e4fd85a8ac1727867a52c40a74c61505'}&units=metric"
    
    # Sending a GET request to the API and storing the response
    response = requests.get(base_url)
    
    # Converting the response to JSON format
    weather_data = response.json()
    
    # Checking if the location field is empty
    if not location:
        reset()
        error_message.config(text='Please fill the input field')  # Displaying an error message if location is not provided
    else:
        # Handling successful API response (HTTP status code 200)
        if response.status_code == 200:
            # Displaying temperature, humidity, wind speed, pressure, and precipitation data
            temp_lable.config(text=str(f'Temperature: {weather_data['main']['temp']}°C'))
            humidity_lable.config(text=str(f'Humidity: {weather_data['main']['humidity']}%'))
            wind_speed_lable.config(text=str(f'Wind Speed: {weather_data['wind']['speed']}km/h'))
            pressure_lable.config(text=str(f'Pressure: {weather_data['main']['pressure']}hPa'))
            precipitation_lable.config(text=str(f'Precipitation: N/A'))
        # Handling unsuccessful API response (HTTP status code 404 or incorrect location)
        elif response.status_code == 404 or weather_data.get('cod') == '404':
            # Displaying an error message for incorrect location and resetting weather labels to default values
            error_message.config(text='Please enter the correct location')
            reset()
            
# Function to clear error messages
def clear_error_message(e=None):
    error_message.config(text='')

# Function to reset text labels to default values
def reset():
    error_message.config(text='Please enter the correct location')
    temp_lable.config(text=str(f'Temperature: 0'))
    humidity_lable.config(text=str(f'Humidity: 0'))
    wind_speed_lable.config(text=str(f'Wind Speed: 0'))
    pressure_lable.config(text=str(f'Pressure: 0'))
    precipitation_lable.config(text=str(f'Precipitation: 0'))

font_family = 'Arial'
font_size = 14

# Creating the main window for the weather forecast app
window = tk.Tk()
window.title('Welcome to weather forecast app from Almdrasa')  # Setting the window title
window.geometry("450x400")  # Defining the window size

window.bind('<Button-1>', clear_error_message)  # Binding left mouse button click event to clear error message

window.columnconfigure(0, weight=1)  # Configuring column distribution within the window
window.rowconfigure(0, weight=1)  # Configuring row distribution within the window

# Creating a frame to hold the elements of the user interface
frame = tk.Frame(window)
frame.grid(row=0, column=0, sticky='nsew')  # Defining the frame layout within the window
frame.columnconfigure(0, weight=7)  # Configuring column distribution inside the frame
frame.columnconfigure(1, weight=3)  # Configuring column distribution inside the frame

# Creating a label prompting the user to enter the location
label = tk.Label(frame, text="Enter the location", font=(font_family, font_size))
label.grid(row=0, column=0, sticky='nw', padx=5, pady=5)  # Defining the label layout inside the frame

# Creating a search button to trigger the weather data search
btn_search = tk.Button(frame, text='Search', command=search)
btn_search.grid(row=1, column=1, sticky='ew', padx=5, pady=5)  # Defining the search button layout inside the frame

# Creating an entry field for the user to input the location
search_input = tk.Entry(frame)
search_input.grid(row=1, column=0, sticky='ew', padx=5, pady=5)  # Defining the entry field layout inside the frame
search_input.bind('<FocusIn>', clear_error_message)  # Binding the focus in event to clear error message
search_input.bind('<Return>', lambda event: search())

# Creating labels to display weather information (temperature, humidity, wind speed, pressure, precipitation)
temp_lable = tk.Label(frame, text='Temperature: 0', font=(font_family, font_size))
temp_lable.grid(row=2, column=0, sticky='nw', padx=5, pady=5)  # Defining the temperature label layout inside the frame

humidity_lable = tk.Label(frame, text='Humidity: 0', font=(font_family, font_size))
humidity_lable.grid(row=3, column=0, sticky='nw', padx=5, pady=5)  # Defining the humidity label layout inside the frame

wind_speed_lable = tk.Label(frame, text='Wind Speed: 0', font=(font_family, font_size))
wind_speed_lable.grid(row=4, column=0, sticky='nw', padx=5, pady=5)  # Defining the wind speed label layout inside the frame

pressure_lable = tk.Label(frame, text='Pressure: 0', font=(font_family, font_size))
pressure_lable.grid(row=5, column=0, sticky='nw', padx=5, pady=5)  # Defining the pressure label layout inside the frame

precipitation_lable = tk.Label(frame, text='Precipitation: 0', font=(font_family, font_size))
precipitation_lable.grid(row=6, column=0, sticky='nw', padx=5, pady=5)  # Defining the precipitation label layout inside the frame

error_message = tk.Label(frame, text='', font=(font_family, font_size), fg="red")
error_message.grid(row=7, column=0, sticky='nw', padx=5, pady=5)  # Defining the error message label layout inside the frame

window.mainloop()  # Running the main event loop to display the user interface
