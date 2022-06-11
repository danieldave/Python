print ("This Program converts Celsius degrees to Fahrenheit")

def Fahrenheit(celcius):
    Fahrenheit = float (celcius) * 9/5 + 32
    return Fahrenheit

def Celcius(fahrenheit):
    celcius = (float(fahrenheit) - 32) * 5/9
    return celcius

print ("Enter the Value available and ignore the other")

celcius = input("Enter the value of celcius: ")
fahrenheit = input("Enter the value of fahrenheit: ")

action = input("What conversion would you like to do? C for celcius and F for Fahrenheit : ")
if action == "C":
    print (Fahrenheit(celcius))
elif action == "F":
    print (Celcius(fahrenheit))
else:
    print("Invalid Selection")