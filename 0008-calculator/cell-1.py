def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    result = 0
    try:
        return x / y
    except ZeroDivisionError:
        print("Error: you can't divide by zero!")

def floorDivision(x, y):
    try:
        return x // y
    except ZeroDivisionError:
        print("Error: you can't divide by zero!")

def modulus(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        print("Error: you can't divide by zero!")

def exponentiation(x, y):
    return x ** y

# Test functions
x = 5
y = 3
print("== Start: Test Calculation Functions ==")
print(f"Add {x} and {y}:", add(x, y))
print(f"Subtract {x} from {y}:", subtract(x, y))
print(f"Multiply {x} and {y}:", multiply(x, y))
print(f"Divide {x} by {y}:", divide(x, y))
print(f"Floor divide {x} from {y}:", floorDivision(x, y))
print(f"Find the remainder of {x} from {y}:", modulus(x, y))
print(f"Find the exponent of {x} from {y}:", exponentiation(x, y))
print("== End: Test Calculation Functions ==")