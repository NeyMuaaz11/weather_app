import requests

query = input("Search for a city...\n")

params = {'key':'f68f78080ffc4dc7863174330202207',
          'q':query}

r = requests.get("http://api.weatherapi.com/v1/current.json", params = params)

data = r.json()

city = data['location']['name']
region = data['location']['region']
country = data['location']['country']
time = data['location']['localtime']
temp = data['current']['temp_c']
feels_like = data['current']['feelslike_c']
humidity = data['current']['humidity']
wind_dir = data['current']['wind_dir']
wind_speed = data['current']['wind_kph']
wind_angle = data['current']['wind_degree']
condition = data['current']['condition']['text']
visibility = data['current']['vis_km']

print(f"{city}, {region}, {country}\n{time}")
print(f"Temperature: {temp}\nFeels like: {feels_like}\nHumidity: {humidity}")
print(f"Skies: {condition}\nVisibility: {visibility}")
print(f"Wind Speed: {wind_speed}\nWind direction: {wind_angle} in {wind_dir}")