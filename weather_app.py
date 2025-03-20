import requests
from datetime import datetime

# OpenWeatherMap API key
API_KEY = "12fdd0be7ba7bbcb19c3a88a0dfa3c70"

def get_weather(city):
    # API endpoint and parameters
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    # Check for errors in the API response
    if "cod" in data and data["cod"] != 200:
        print(f"Error: {data.get('message', 'Unknown error')}")
        return

    # Extract weather data
    main = data["main"]
    weather = data["weather"][0]
    wind = data["wind"]
    sys = data["sys"]

    temperature = main["temp"]
    humidity = main["humidity"]
    description = weather["description"]
    wind_speed = wind["speed"]
    sunrise = datetime.fromtimestamp(sys["sunrise"]).strftime('%H:%M')
    sunset = datetime.fromtimestamp(sys["sunset"]).strftime('%H:%M')

    # Display weather details
    print(f"Weather in {city}:")
    print(f"  Temperature: {temperature}°C")
    print(f"  Humidity: {humidity}%")
    print(f"  Condition: {description.capitalize()}")
    print(f"  Wind Speed: {wind_speed} m/s")
    print(f"  Sunrise: {sunrise}")
    print(f"  Sunset: {sunset}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
    input("Press Enter to exit...")