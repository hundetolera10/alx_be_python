#!/usr/bin/python3
"""
Temperature Conversion Tool
Demonstrates global variables and functions for Celsius <-> Fahrenheit conversion
"""

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


if __name__ == "__main__":
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        elif unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print("Invalid temperature. Please enter a numeric value.")
