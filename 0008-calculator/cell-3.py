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

print("== Welcome to Davina's Calculator ==")
x = float(input("Please give a number (decimals and negative numbers are allowed):"))
y = float(input("Please give another number (decimals and negative numbers are allowed):"))

print("Here are the available arithmetic operators:")
for op_symbol, op_info in operators.items():
    name = op_info["name"]
    description = op_info["description"]
    print(f"\t'{op_symbol}' - {name}: {description}")

operator = input("Choose one:")
print(calculator(x, y, operator))