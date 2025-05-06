# 🎮 Davina's Tic Tac Toe (Noughts and Crosses)

This notebook demonstrates a basic implementation of a single-move **Tic Tac Toe** game (also known as _Noughts and Crosses_) using Python. It initializes a 3x3 board, allows a player to input their move, and checks for a win condition.

---

## 🧱 1. Board Initialization

```python
symbols = ["O", "X", "."]
```

- `"O"` and `"X"` are player symbols.
- `"."` represents an empty cell on the board.

The board is a 3x3 grid initialized with `"."`:

```python
board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]
```

---

## 👀 2. Display Functions

### `show_symbols(symbols)`

Prints the available symbols (used for clarity or debugging).

### `show_board(board)`

Prints the current state of the board row by row.

---

## 🏆 3. Win Condition Check

### `check_win(board, symbol)`

Checks if the given player (`symbol`) has won:

- ✅ Three in a row (horizontal)
- ✅ Three in a column (vertical)
- ✅ Three diagonally (left-to-right or right-to-left)

---

## 🎮 4. User Interaction (Single Move)

The user is prompted to:

1. Enter a row number (`y`) between 0 and 2
2. Enter a column number (`x`) between 0 and 2
3. Choose a symbol (`O` or `X`) to place at the chosen spot

Input is validated for:

- Out-of-bounds indices
- Invalid symbols
- Attempting to place outside the board

If valid:

- The symbol is placed on the board
- The board is updated and printed
- A win check is performed immediately after the move

---

## ❗ Limitations

- Only one move is processed per run.
- No loop for alternating turns.
- No check for full-board draw conditions.
- No prevention of placing a symbol on an occupied cell.

---

## ✅ Sample Output

```
=== Welcome to Davina's Tic Tac Toe ===
Here's the board:
['.', '.', '.']
['.', '.', '.']
['.', '.', '.']

Give a value between 0 and 2: 0
Give another value between 0 and 2: 0
Which symbol do you want to place at that spot (O/X)? O

Here's the board:
['O', '.', '.']
['.', '.', '.']
['.', '.', '.']

O won!  # (only if it happens to be a winning move)
```

---

## 📚 Next Steps

To turn this into a full game:

- Add a loop for alternating turns between players
- Track game state and move count
- Check for draw conditions when the board is full
- Prevent overwriting existing symbols

---
