import requests  # type: ignore

# Replace with your own API key
api_key = "1432a1c5e57a0ba064c48766334cd1e5"
# City for which you want the weather
city = "India"
# Base URL for OpenWeatherMap API
base_url = "https://api.openweathermap.org/data/2.5/weather"

# Set up parameters
params = {
    'q': city,
    'appid': api_key,
    'units': 'metric'  # use 'imperial' for Fahrenheit
}

# Make a request
response = requests.get(base_url, params=params)

# Convert the response to JSON
weather_data = response.json()

# Print the weather information
if weather_data.get('cod') == 200:
    print(f"Weather in {city}: {weather_data['weather'][0]['description']}")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
else:
    print("Error:", weather_data.get("message", "Cannot fetch weather data"))
