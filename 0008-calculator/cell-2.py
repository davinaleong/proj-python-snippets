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

def calculator(x, y, operator):
    message = ""
    if operator not in operators:
        message = f"Operator '{operator}' is undefined."
        
    if operator in ("/", "//", "%"):
        try:
            if operator == "/":
                result = divide(x, y)
                message = f"{x} divided by {y} is {result}."
            if operator == "//":
                result = floorDivision(x, y)
                message = f"The floor of {x} divided by {y} is {result}."
            if operator == "%":
                result = modulus(x, y)
                message = f"The remainder of {x} divided by {y} is {result}."
        except ZeroDivisionError:
            message = "Error: you can't divide by zero!"
    elif operator in ("+", "-", "*", "**"):
        if operator == "+":
            result = add(x, y)
            message = f"{x} added to {y} is {result}."
        if operator == "-":
            result = subtract(x, y)
            message = f"{x} subtracted from {y} is {result}."
        if operator == "*":
            result = multiply(x, y)
            message = f"{x} multiplied by {y} is {result}."
        if operator == "**":
            result = modulus(x, y)
            message = f"The exponent of {x} by {y} is {result}."

    return message

# Test functions
x = 5
y = 3
print("== Start: Test Calculator Functions ==")
print(calculator(x, y, "+"))
print(calculator(x, y, "-"))
print(calculator(x, y, "*"))
print(calculator(x, y, "/"))
print(calculator(x, y, "//"))
print(calculator(x, y, "%"))
print(calculator(x, y, "**"))
print("== End: Test Calculator Functions ==")