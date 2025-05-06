print("=== Welcome to Davina's Tic Tac Toe ===")

symbols = ["O", "X", "."]

board = [
    [symbols[2], symbols[2], symbols[2]],
    [symbols[2], symbols[2], symbols[2]],
    [symbols[2], symbols[2], symbols[2]],
]

def show_symbols(symbols):
    print("These are the available symbols:")
    print(symbols)


def show_board(board):
    print("Here's the board:")
    for row in board:
        print(row)

def check_win(board, symbol):
    # Check rows
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == symbol for i in range(3)):
        return True

    if all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False
    
show_board(board)

y = int(input("Give a value between 0 and 2:"))
if y > len(board) - 1:
    print(f"Error: y must be between 0 and 2.")
else:
    row = board[y]
    x = int(input("Give another value between 0 and 2"))
    if x > len(row) - 1:
        print(f"Error: x must be between 0 and 2.")
    else:
        symbol = input("Which symbol do you want to place at that spot (O/X)?")
        if symbol not in symbols:
            print(f"Error: symbol '{symbol}' not found.")
        else:
            board[y][x] = symbol
            show_board(board)
            if check_win(board, symbol): print(f"{symbol} won!")