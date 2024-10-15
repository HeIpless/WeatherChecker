import requests
import time
import os

def clean():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_ip_address():
    response = requests.get("https://api.ipify.org/?format=json")
    return response.json()['ip']

def get_weather(location):
    url = f"https://api.weatherapi.com/v1/current.json?key=bbbb798f670b470ab42171540241310&q={location}"
    response = requests.get(url)
    return response.json()


def display_weather(weather_data):
    print("City:", weather_data['location']['name'])
    print("Region:", weather_data['location']['region'])
    print("Currently:", weather_data['current']['temp_f'], "degrees Fahrenheit")
    print("Feels like:", weather_data['current']['feelslike_f'], "degrees Fahrenheit")
    print("Condition:", weather_data['current']['condition']['text'])
    print("Wind Speed:", weather_data['current']['wind_mph'], "mph")
    print("Humidity:", weather_data['current']['humidity'], "%")
    print("UV Index:", weather_data['current']['uv'])
    print("Cloud Coverage:", weather_data['current']['cloud'], "%")


def check_ip_address():
    user_input = input("Do you want to check your IP address before starting? (y/n): ").lower()
    if user_input == 'y' or user_input == 'yes':
        ip = get_ip_address()
        print("Your IP Address is:", ip)


def get_location():
    location_input = input("Enter a location (city, country) or press Enter to use your IP-based location: ").strip()
    if not location_input:
        print("No location entered. Using IP-based location...")
        ip = get_ip_address()
        # Use IP-based location (assuming the service provides it)
        location_data = requests.get(f"https://ipinfo.io/{ip}/json").json()
        location_input = location_data['city'] + ',' + location_data['region']
    return location_input


def main():
    # Clear screen at the start
    clean()

    # Check IP address
    check_ip_address()

    # Get the user's location
    location = get_location()

    # Fetch weather data
    print(f"Checking weather for {location}...")
    weather_data = get_weather(location)

    # Display the weather data
    display_weather(weather_data)

    # Clean the screen after displaying weather
    time.sleep(5)
    clean()

    # Countdown before closing
    for i in range(3, 0, -1):
        print(f"Program closing in {i} seconds...")
        time.sleep(1)
        clean()

# Run the main function
if __name__ == "__main__":
    main()
