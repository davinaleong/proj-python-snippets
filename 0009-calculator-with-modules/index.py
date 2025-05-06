from calculator import *

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