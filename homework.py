#W3
city = input("What is the name of the city? ")
temp = input("What is the temp in Celcius? ")

def C_to_F(temp):
    fahrenheit = float(temp) * 9/5 + 32
    
    return fahrenheit

rTemp = C_to_F(temp)
print (f'It is currently {temp}ºC ({round(rTemp)}ºF) in {city}')