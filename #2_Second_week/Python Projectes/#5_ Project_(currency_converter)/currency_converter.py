import requests

def convert_currency(api_key, from_currency, to_currency, amount):
    # Construct the API URL with the provided parameters
    url = f"https://api.apilayer.com/fixer/convert?apikey={api_key}&from={from_currency}&to={to_currency}&amount={amount}"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the response status is successful (status code 200)
    if response.status_code == 200:
        # Convert the response to JSON format
        data = response.json()
        # Retrieve the converted amount from the response data
        converted_amount = data.get('result')
        # Print the converted amount with currencies
        print(f"{amount} {from_currency} equals {converted_amount} {to_currency}")
    else:
        # If the request fails, print an error message
        print("Failed to convert. Please try again later.")

api_key = '8juraaxZMK8Vf8AsZMKJyKZ7LF5lpmD9'  # API key

# Prompt the user to input source and target currencies, and the amount to convert
from_currency = input("Enter the source currency: ")
to_currency = input("Enter the target currency: ")
amount = float(input("Enter the amount to convert: "))

# Call the convert_currency function with user inputs
convert_currency(api_key, from_currency, to_currency, amount)
