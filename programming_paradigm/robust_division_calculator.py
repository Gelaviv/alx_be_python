def safe_divide (numerator, denominator):
    try:
        num_float = float(numerator)
        denom_float = float(denominator)
        result = num_float/denom_float
        return (f"The result of the division is {result}")
    except ValueError:
        return("Error: Please enter numeric values only.")
    except ZeroDivisionError:
        return("Error: Cannot divide by zero.")