# Get the number of apples that the customer has bought.
str_num_of_apples = input("Enter the number of apples you have.")

# Get the number of oranges that the customer has bought.
str_num_of_oranges = input("Enter the number of oranges you have.")

# Cast the number of apples into a string
num_of_apples = int(str_num_of_apples)

# Cast the number of oranges into a string
num_of_oranges = int(str_num_of_oranges)

# Get the total number of fruits that the customer has
num_total_fruits = num_of_apples + num_of_oranges

# Construct the print statement into something human-friendly
str_total_fruits = f"{str_num_of_apples} apples and {str_num_of_oranges} oranges amounts to {num_total_fruits} fruits."

print(str_total_fruits)