FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
   

num_to_convert = float(input("Enter the temperature to convert: "))
degree = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()
if degree == "F":
    celsius = convert_to_celsius(num_to_convert)
    print(f"{num_to_convert}°F is {celsius}°C")
elif degree == "C":
    fahrenheit = convert_to_fahrenheit(num_to_convert)
    print(f"{num_to_convert}°C is {fahrenheit}°F")
else:
    print("Invalid unit. Please enter either C or F.")