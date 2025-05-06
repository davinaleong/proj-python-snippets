fruit_line = '🍎🍏🍐🍊🍋🍌🍉🍇🍓🫐🍈🍒🍑🥭🍍🥥🥝🍅🫒'
max_index = len(fruit_line) - 1

start_index = int(input(f'Pick a starting index between 0 and {max_index}:'))
end_index = int(input(f'Pick an ending index between 0 and {max_index}, different from {start_index}:'))

# Ensure the start index is less than the end index
if start_index > end_index:
    start_index, end_index = end_index, start_index

selected_fruits = fruit_line[start_index:end_index]
print(f'\nYour selected fruits: {selected_fruits}')