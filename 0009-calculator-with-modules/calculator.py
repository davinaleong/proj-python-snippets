# Import all functions (add, subtract, multiply, divide, etc.) from the calculations module
from calculations import *

# Dictionary defining supported operators and their details
operators = {
    "+": {
        "name": "Add",
        "description": "Add things together",
    },
    "-": {
        "name": "Subtract",
        "description": "Take one thing away from another",
    },
    "*": {
        "name": "Multiply",
        "description": "Multiply (like repeated addition)",
    },
    "/": {
        "name": "Divide",
        "description": "Divide (split into equal parts)",
    },
    "//": {
        "name": "Floor Division",
        "description": "Divide and drop the decimals (only whole number part)",
    },
    "%": {
        "name": "Modulus",
        "description": "Get what’s left over after dividing (the remainder)",
    },
    "**": {
        "name": "Exponentiation",
        "description": "Raise a number to a power (like 2 to the power of 3)"
    },
}

# Calculator function that performs the specified operation on two numbers
def calculator(x, y, operator):
    message = ""  # Initialize an empty message string

    # Check if the operator is not defined in the operators dictionary
    if operator not in operators:
        message = f"Operator '{operator}' is undefined."
        
    # Handle division-related operations, which can raise ZeroDivisionError
    if operator in ("/", "//", "%"):
        try:
            if operator == "/":
                result = divide(x, y)  # Call divide function from calculations
                message = f"{x} divided by {y} is {result}."
            if operator == "//":
                result = floorDivision(x, y)  # Call floorDivision function
                message = f"The floor of {x} divided by {y} is {result}."
            if operator == "%":
                result = modulus(x, y)  # Call modulus function
                message = f"The remainder of {x} divided by {y} is {result}."
        except ZeroDivisionError:
            message = "Error: you can't divide by zero!"
    
    # Handle arithmetic operations
    elif operator in ("+", "-", "*", "**"):
        if operator == "+":
            result = add(x, y)  # Call add function
            message = f"{x} added to {y} is {result}."
        if operator == "-":
            result = subtract(x, y)  # Call subtract function
            message = f"{x} subtracted from {y} is {result}."
        if operator == "*":
            result = multiply(x, y)  # Call multiply function
            message = f"{x} multiplied by {y} is {result}."
        if operator == "**":
            result = exponentiation(x, y)  # Corrected to call exponentiation function
            message = f"The exponent of {x} by {y} is {result}."

    return message  # Return the final result message
