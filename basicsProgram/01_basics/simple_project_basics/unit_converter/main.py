# 01_basics/simple_project_basics/unit_converter.py
# Convert between units
def meters_to_feet(meters):
    return meters * 3.28084

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("10 meters to feet:", meters_to_feet(10))
print("25°C to Fahrenheit:", celsius_to_fahrenheit(25))