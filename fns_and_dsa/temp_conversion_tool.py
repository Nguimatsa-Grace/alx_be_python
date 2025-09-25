# Define global conversion factors for Fahrenheit to Celsius and vice-versa.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): The temperature in Fahrenheit.

    Returns:
    float: The converted temperature in Celsius.
    """
    # Use the global conversion factor to perform the calculation.
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Parameters:
    celsius (float): The temperature in Celsius.

    Returns:
    float: The converted temperature in Fahrenheit.
    """
    # Use the global conversion factor to perform the calculation.
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    """
    Main function to handle user interaction and temperature conversion.
    """
    try:
        # Prompt the user for temperature input.
        temperature_str = input("Enter the temperature to convert: ")
        temperature = float(temperature_str)

        # Prompt the user for the unit.
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'F':
            # Convert from Fahrenheit to Celsius and print the result.
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            # Convert from Celsius to Fahrenheit and print the result.
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            # Handle invalid unit input.
            print("Invalid unit. Please enter 'C' or 'F'.")

    except ValueError:
        # Handle non-numeric temperature input.
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
