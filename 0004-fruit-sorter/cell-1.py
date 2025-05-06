apples = int(input('Enter the number of apples:'))
bananas = int(input('Enter the number of bananas:'))
oranges = int(input('Enter the number of oranges:'))

max_fruit_quantity = int(input('Set the **high stock threshold** (e.g. 10 or more fruits): '))
min_fruit_quantity = int(input('Set the **low stock warning** level (e.g. 5 or fewer fruits): '))

capacity = int(input('Enter the basket capacity:'))

# Basket counters
apple_basket = 0
banana_basket = 0
orange_basket = 0

# Comparisons and increments
print('=== Start of Fruit Comparison ===')
if apples > bananas and apples > oranges:
    print('🍎 is the most!')
    apple_basket += 1
elif bananas > apples and bananas > oranges:
    print('🍌 is the most!')
    banana_basket += 1
elif oranges > apples and oranges > bananas:
    print('🍊 is the most!')
    orange_basket += 1
else:
    print('There is a tie for the most fruits!')

# Use of equality and inequality
if apples == bananas:
    print('🍎 == 🍌')
if oranges != bananas:
    print('🍊 != 🍌')

# Use of >=, <=
if apples >= max_fruit_quantity:
    print(f'You have at least {max_fruit_quantity} 🍎!')
if bananas >= max_fruit_quantity:
    print(f'You have at least {max_fruit_quantity} 🍌!')
if oranges >= max_fruit_quantity:
    print(f'You have at least {max_fruit_quantity} 🍊!')
    
if apples <= min_fruit_quantity:
    print('🍎 are running low!')
if bananas <= min_fruit_quantity:
    print('🍌 are running low!')
if oranges <= min_fruit_quantity:
    print('🍊 are running low!')

# Use of += incrementing baskets manually
# For every x apples, add 1 basket
apple_basket += apples // capacity
banana_basket += bananas // capacity
orange_basket += oranges // capacity

# Summary
print('=== Summary ===')
print(f'Basket capacity: {capacity}')
print(f'🍎 baskets: {apple_basket}')
print(f'🍌 baskets: {banana_basket}')
print(f'🍊 baskets: {orange_basket}')