#Ask for a city name
#It is currently C in Paris, France

import requests
from rich import print
from datetime import datetime

def print_day(day, temp):
    """Printing out weather days"""
    print(f'[purple]{day}: {temp}°C[/purple]')

def display_current_temp(city):
    """Displays Today's temp of a city"""
    key = "aabfdd47312t10fba463o35fe43c6a13"
    url = f'https://api.shecodes.io/weather/v1/current?query={city}&key={key}'

    
    #to make api request
    request = requests.get(url)
    #print(request)  => #verify 200 response

    #convert resonse to json
    weather = request.json()
    #print(weather)
    city_name = weather["city"]
    temp = round(weather["temperature"]["current"])
    print(f'\n[yellow bold]Weather for {city_name}[/yellow bold]')
    print_day("Today", temp)
    
def display_forecast(city):
    """Displays forecast"""
    
    key = "aabfdd47312t10fba463o35fe43c6a13"
    url = f'https://api.shecodes.io/weather/v1/forecast?query={city}&key={key}'
    response = requests.get(url)
    forecast = response.json()
    print("\n[green bold]Forecast:[/green bold]") 
    
    
    for each_day in forecast["daily"]:
        timestamp = each_day["time"]
        date = datetime.fromtimestamp(timestamp)
        day = date.strftime("%A")
        temp = each_day["temperature"]["day"]
        if date.date() != datetime.today().date():
            print_day(day, temp)
            
        
    
    
      

print("[blue bold]Welcome to my weather app[/blue bold]")
city = input("Enter a city...")
city = city.strip()

if city:
    display_current_temp(city)
    display_forecast(city)
else: 
    print("oops...that's not a city name. Please try again")
    
print("\n[blue]This app was coded by Ash Sahin[/blue]")










