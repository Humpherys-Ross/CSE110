# calculates the wind chill temperature for a given air temperature
# and wind speed
def calculate_wind_chill(temperature, wind_speed):
    # Calculate the wind chill temperature
    if temperature < 50 and wind_speed >= 3:
        wind_chill = (35.74 + 0.6215 * temperature - 35.75 *
                      (wind_speed ** 0.16) + 0.4275 * temperature *
                      (wind_speed ** 0.16))
        # Return the wind chill temperature
        return wind_chill
    else:
        # Return None if the wind chill temperature cannot be calculated
        return None


# calculates the temperature in Fahrenheit from a given temperature in Celsius
def celsius_to_fahrenheit(celsius_temperature):
    # Return the temperature in Fahrenheit
    return (celsius_temperature * 9/5) + 32


# Input temperature and unit (Fahrenheit or Celsius)
temperature = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()

# Convert Celsius to Fahrenheit if needed
if unit == 'C':
    temperature = celsius_to_fahrenheit(temperature)

# Display the wind chill values for various wind speeds
print(
    f"At temperature {temperature}F, and wind speed 5 mph, the windchill is: "
    f"{calculate_wind_chill(temperature, 5):.2f}F")
# Display the wind chill values for various wind speeds
# starting at 10 mph uo to 60 mph in 5 mph increments
for wind_speed in range(10, 61, 5):
    wind_chill = calculate_wind_chill(temperature, wind_speed)
    if wind_chill is not None:
        print(f"At temperature {temperature}F, and wind speed {wind_speed} "
              f"mph, the windchill is: {wind_chill:.2f}F")
