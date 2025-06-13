FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR 
    FAHRENHEIT_TO_CELSIUS_FACTOR = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    
    return FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR 
    CELSIUS_TO_FAHRENHEIT_FACTOR =(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    
    return CELSIUS_TO_FAHRENHEIT_FACTOR

temperature = float(input("Enter the temperature to convert: "))
c_or_f = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()

if c_or_f == "F":
    convert_to_celsius(temperature)
    print(f"{temperature} F is {FAHRENHEIT_TO_CELSIUS_FACTOR} C")
elif c_or_f == "C":
    convert_to_fahrenheit(temperature)
    print(f"{temperature} C is {CELSIUS_TO_FAHRENHEIT_FACTOR} F")
else:
    print("Invalid temperature. Please enter a numeric value.")

