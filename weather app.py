import requests


def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

def display_weather(data):
    name = data['name']
    weather = data['weather'][0]['description'].title()
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    print(f"\nWeather in {name}:")
    print(f"  {weather}")
    print(f"  Temperature: {temp}°C (Feels like {feels_like}°C)")
    print(f"  Humidity: {humidity}%")
    print(f"  Wind Speed: {wind} m/s\n")

def main():
    print("=== Creative CLI Weather App ===")
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    while True:
        city = input("Enter city name (or 'quit' to exit): ").strip()
        if city.lower() == 'quit':
            print("Goodbye! Stay weather-wise! ☀️🌧️")
            break
        data = get_weather(city, api_key)
        if data:
            display_weather(data)
        else:
            print("City not found or API error. Please try again.")

if __name__ == "__main__":
    main()