# Inputs for fruit prices
str_apple_price = input('Enter the price of a single apple: ')
str_banana_price = input('Enter the price of a single banana: ')
str_durian_price = input('Enter the price of a single durian: ')

# Inputs for fruits bought
str_apples_bought = input('How many apples did you buy? ')
str_bananas_bought = input('How many bananas did you buy? ')
str_durians_bought = input('How many durians did you buy? ')

# Fruit prices
apple_price = float(str_apple_price)
banana_price = float(str_banana_price)
durian_price = float(str_durian_price)

# Quantities
apples_bought = int(str_apples_bought)
bananas_bought = int(str_bananas_bought)
durians_bought = int(str_durians_bought)

# Free apples
free_apples = apples_bought // 2  # 1 free for every 2 bought
total_apples = apples_bought + free_apples

# Total cost before tax
cost = (apples_bought * apple_price) + (bananas_bought * banana_price) + (durians_bought * durian_price)

# Apply tax (9%)
tax_rate = 0.09
tax_amount = cost * tax_rate
total_cost = cost + tax_amount

# Average price per fruit (including free apples)
total_fruits = total_apples + bananas_bought + durians_bought
average_price = total_cost / total_fruits

# Floor division and modulus for durian price
dollar_part = durian_price // 1
cent_part = durian_price % 1

# Exponentiation (bonus): Square the number of bananas
banana_power = bananas_bought ** 2

# Print results
print(f"\n=== Fruit Shop Summary ===")
print(f"Free apples received: {free_apples}")
print(f"Total cost after 9% tax: SGD{total_cost:.2f}")
print(f"Average price per fruit: SGD{average_price:.2f}")
print(f"Durian price breakdown: SGD{int(dollar_part)} and {int(cent_part * 100)} cents")
print(f"Bananas squared: {banana_power}")