#W3
city = input("What is the name of the city? ")
temp = input(f'What is the temp(in Celcius) in {city.capitalize()}? ')
temp = int(temp)


def C_to_F(temp):
    fahrenheit = float(temp) * 9/5 + 32   
    return fahrenheit

def display(city, temp):
    rTemp = C_to_F(temp)
    print (f'It is currently {temp}ºC ({round(rTemp)}ºF) in {city.capitalize()}')
   
display(city, temp) 

