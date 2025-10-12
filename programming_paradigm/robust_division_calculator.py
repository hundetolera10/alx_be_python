# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with error handling for:
    - Division by zero
    - Non-numeric inputs
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Perform the division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
