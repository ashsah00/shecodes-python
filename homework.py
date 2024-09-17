#W3L3    
def city_temp(city, temp):
    """Displays city and temp"""
    print(f'The temperature in {city} is {temp}')

print(help(city_temp))
city_temp("rockville", 79)
city_temp("lisbon", 68)


#W3 L2
"""
def city_temp():
    city = input("Which city are you in: ")
    city = city.capitalize()
    temp = input("What is the temp?: ")

    if city and temp:
        print(f'You are in {city} and it is currently {temp}ºF')
    else:
        print("Please enter both city and temp!")
        
city_temp()   
city_temp()   
"""