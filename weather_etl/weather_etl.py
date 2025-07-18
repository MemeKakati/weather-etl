from datetime import datetime #to get the current date
import requests #call the API
import pandas as pd #import pandas to transform and clean the data


#Extract (Get the Data)
API_KEY = '932bc329e1d510770fc2aabaedb2616a'
CITY = 'Louisville'
UNITS = 'imperial' #use 'metric' for Celsius

# Define the URL for the OpenWeatherMap API
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}'
response = requests.get(URL) # Get the response from the API
data = response.json() # Converts the response into a python dictionary

#Transform (Clean the Data)
weather_data = {
    'City': CITY,
    'datetime': datetime.utcfromtimestamp(data['dt']), # Convert UNIX timestamp to readable date and time
    'temperature': data['main']['temp'], # Current temperature
    'feels_like': data['main']['feels_like'], # Temperature that feels like
    'humidity': data['main']['humidity'], # Humidity percentage
    'weather_main': data['weather'][0]['main'], # Main weather condition
    'weather_description': data['weather'][0]['description'], # Detailed weather description
    'wind_speed': data['wind']['speed'] # Wind speed
}

df = pd.DataFrame([weather_data]) # Create a DataFrame from the dictionary (table format)

#Load (Save the Data)
output_file = 'weather_data.csv' # Define the output file name
df.to_csv(output_file, index=False) # Save the DataFrame to a CSV file
print(f"Weather data for {CITY} has been saved to {output_file}.") # Confirmation message

