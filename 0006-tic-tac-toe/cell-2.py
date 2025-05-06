print("=== Welcome to Davina's Tic Tac Toe ===")

symbols = ["O", "X"]
placeholder = "."
board = [
    [placeholder, placeholder, placeholder],
    [placeholder, placeholder, placeholder],
    [placeholder, placeholder, placeholder],
]

def show_board(board):
    for row in board:
        print(" | ".join(row))
    print()

def check_win(board, symbol):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or \
           all(board[j][i] == symbol for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)) or \
       all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != placeholder for row in board for cell in row)

# Game loop
current_player = 0  # 0 for O, 1 for X

while True:
    show_board(board)
    print(f"Player {symbols[current_player]}'s turn.")
    
    try:
        y = int(input("Enter row (0-2): "))
        x = int(input("Enter column (0-2): "))
        
        if board[y][x] != placeholder:
            print("That spot is already taken. Try again.\n")
            continue

        board[y][x] = symbols[current_player]

        if check_win(board, symbols[current_player]):
            show_board(board)
            print(f"Player {symbols[current_player]} wins!")
            break

        if is_full(board):
            show_board(board)
            print("It's a draw!")
            break

        current_player = 1 - current_player  # Switch player

    except (ValueError, IndexError):
        print("Invalid input. Please enter numbers between 0 and 2.\n")
