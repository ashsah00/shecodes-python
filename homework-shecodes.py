#Ask for a city name
#It is currently C in Paris, France

import requests
from rich import print

city = input("Enter a city name...")
key = "aabfdd47312t10fba463o35fe43c6a13"
url = f'https://api.shecodes.io/weather/v1/current?query={city}&key={key}'


#to make api request
request = requests.get(url)
#print(request)  => #verify 200 response

#convert resonse to json
weather = request.json()
#print(weather)

temp = round(weather["temperature"]["current"])
city = weather["city"]
country = weather["country"]

print(f'It is currently {temp}°C in {city}, {country}.')