#Exercise 1
weather = {
    "city":"Lisbon",
    "country":"Portugal",
    "temperature":17.94,
    "humidity":77
}


fahrenheit = (weather["temperature"] * 9/5) + 32

print(f'It is {round(weather["temperature"])}°C ({round(fahrenheit)}°F) in {weather["city"]}, {weather["country"]}. The humidity level is {weather["humidity"]}%.')

#Exercise 2
forecast = {
    "city":"Lisbon",
    "county":"Portugal",
    "daily": [
        17.76,
        13.08,
        12.14,
        11.25,
        14.29
    ]
}

print(f'The forecast for {forecast["city"]}, {forecast["county"]} for the next five days is:')
index = 0
for daily, temp in forecast.items():
    print(f'Day {index + 1}: {forecast["daily"][index]}')
    index +=1
