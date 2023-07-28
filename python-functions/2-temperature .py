#!/usr/bin/python3
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius 

temperature_fahrenheit = 68
temperature_celsius = convert_to_celsius(temperature_fahrenheit)
print(f"{temperature_fahrenheit}°F is equal to {temperature_celsius:.2f}°C")



def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

temperature_fahrenheit = 68
temperature_celsius = convert_to_celsius(temperature_fahrenheit)
print(f"{temperature_fahrenheit}°F is equal to {temperature_celsius:.2f}°C")

print(convert_to_celsius(100))
print(convert_to_celsius(-40))
print(convert_to_celsius(-459.67))
print(convert_to_celsius(32))