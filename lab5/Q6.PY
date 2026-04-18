# List of temperatures in Fahrenheit
fahrenheit_temps = [32, 50, 77, 100.4, 212]
print("Temperatures in Fahrenheit:", fahrenheit_temps)

celsius_temps = []

for f in fahrenheit_temps:
    # Apply the conversion formula
    c = (f - 32) * 5 / 9
    
    # round(c, 2) limits the decimal to 2 places to make it look clean
    celsius_temps.append(round(c, 2)) 

print("Temperatures in Celsius:", celsius_temps)