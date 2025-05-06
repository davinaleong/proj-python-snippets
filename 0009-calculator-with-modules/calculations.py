# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract the second number from the first
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide the first number by the second
def divide(x, y):
    try:
        return x / y  # Perform division
    except ZeroDivisionError:
        print("Error: you can't divide by zero!")  # Handle division by zero

# Function to perform floor division (integer division)
def floorDivision(x, y):
    try:
        return x // y  # Perform floor division
    except ZeroDivisionError:
        print("Error: you can't divide by zero!")  # Handle division by zero

# Function to calculate the modulus (remainder)
def modulus(x, y):
    try:
        return x % y  # Perform modulus operation
    except ZeroDivisionError:
        print("Error: you can't divide by zero!")  # Handle division by zero

# Function to raise the first number to the power of the second
def exponentiation(x, y):
    return x ** y  # Perform exponentiation
