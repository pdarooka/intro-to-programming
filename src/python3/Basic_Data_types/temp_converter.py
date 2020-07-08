# Basic Data Types: Temperature converter

# Welcome message
print("Welcome!")

# Gets user's inputs
temperature = float(input("Please enter the temperature in degrees Celsius: "))

# Processes and Outputs converted temperatures
print("\nDegrees Fahrenheit:\t", round((temperature * 9/5) + 32, 4))
print("Degrees Celsius:\t", round(temperature, 4))
print("Degrees Kelvin:\t", round(temperature + 273.15, 4))
