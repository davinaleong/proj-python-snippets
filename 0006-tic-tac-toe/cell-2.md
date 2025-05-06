# 🎮 Davina's Full Tic Tac Toe Game (Game Loop Version)

This notebook features a fully playable version of **Tic Tac Toe (Noughts and Crosses)** in Python. Two players take turns placing `"O"` and `"X"` on a 3x3 board. The game ends when one player wins or the board is full (a draw).

---

## 🧱 1. Game Setup

### Symbols:

```python
symbols = ["O", "X"]
placeholder = "."
```

- `"O"` and `"X"` are used by players.
- `"."` represents an empty cell on the board.

### Board:

```python
board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]
```

A 3x3 matrix (list of lists) initialized with placeholders.

---

## 📺 2. Functions

### `show_board(board)`

Prints the board in a readable grid format:

```
. | . | .
. | . | .
. | . | .
```

### `check_win(board, symbol)`

Checks if a player (`symbol`) has a winning combination:

- All 3 cells in any **row**
- All 3 cells in any **column**
- All 3 cells in either **diagonal**

### `is_full(board)`

Returns `True` if the board has no `"."` left (i.e., the game is a draw).

---

## 🔁 3. Game Loop

### Key Mechanics:

- Players alternate turns using `current_player` (0 or 1).
- Prompts for `row` and `column` inputs.
- Validates:
  - That the input is within bounds (0–2)
  - That the selected cell is empty
- Places the player’s symbol in the chosen cell.
- After each move:
  - Checks if the current player has won.
  - Checks if the board is full (draw).
  - Switches to the other player if the game continues.

### Loop Termination:

The loop ends when:

- A player wins
- The board is full (no more valid moves)

---

## ✅ Sample Gameplay

```
=== Welcome to Davina's Tic Tac Toe ===
. | . | .
. | . | .
. | . | .

Player O's turn.
Enter row (0-2): 0
Enter column (0-2): 0

O | . | .
. | . | .
. | . | .

Player X's turn.
...
Player X wins!
```

---

## 🛠️ Possible Enhancements

- Add input for player names
- Add score tracking across rounds
- Improve display with row/column labels
- Add replay option after a win or draw
- Prevent accidental overwrite with visual cues

---

## 👩‍💻 Author

Developed by **Davina** as a practice project for learning Python and game logic using Jupyter Notebook.

---
