#W3L5
def C_to_F(fahrenheit):
    celcius = fahrenheit - 32 * (5/9)
    return celcius
F_temp = 80
temp = C_to_F(F_temp)
print(f'It is currently {round(temp)}ºC ({F_temp}ºF) in London)')
"""    

#W3L4 
"""
def city_temp(city = "NY", temp = "10", hum=""):
    message = f'The temperature in {city} is {temp}º'
    if hum:
        message = f'{message} with a humidity of {hum}%'
    print(message)

#print(help(city_temp))
city_temp("London", 7, 40)
city_temp("Sydney", 7)
"""


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

#W3 L2


def city_temp():
    city = input("Which city are you in: ")
    city = city.capitalize()
    temp = input("What is the temp?: ")

    if city and temp:
        print(f'You are in {city} and it is currently {temp}ºF')
    else:
        print("Please enter both city and temp!")
        
city_temp()        


"""
temp = int(input("What is the current temperature: "))
rainy = input("Is it rainy? (yes/no): ")
rainy = rainy.lower()  #convert the output to lower

#option 1
if temp > 20:
  if rainy == "yes":
    print("umbrella")
  else:
    print("sun glasses")
elif temp < 20:
  if rainy == "yes":
    print("jacket & umbrella")
  else:
    print("jacket")


#option 2

if temp > 20 and weather == "no":
  print("Enjoy a sunny day")
elif temp > 20 and weather == "yes":
  print("Don't forget your umbrella")
elif temp < 20 and weather == "no":
  print("Don't forget your coat")
else: 
  print("Don’t forget your umbrella and your jacket")  

"""
