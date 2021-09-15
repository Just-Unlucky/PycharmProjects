import requests

API_KEY = "e1b8c7307dc5d97e97471350f44f8ab7"
city = input("Hey! Please enter a city.")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
data = requests.get(url).json()
temp = data['main']['temp']
humidity = data['main']['humidity']

print(f'In {city} the temperature is {temp}. The humidity is {humidity}.')