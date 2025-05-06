# 📊 Davina's Calculator Notebook Summary

This Jupyter Notebook builds a **simple calculator** in Python using arithmetic operations, structured into three main sections (cells).

---

## 🟡 **Cell 1: Basic Arithmetic Functions**

Defines core functions for:

- Addition (`add`)
- Subtraction (`subtract`)
- Multiplication (`multiply`)
- Division (`divide`) — with `ZeroDivisionError` handling
- Floor Division (`floorDivision`) — with `ZeroDivisionError` handling
- Modulus (`modulus`) — with `ZeroDivisionError` handling
- Exponentiation (`exponentiation`)

At the end, it **tests** these functions with `x = 5` and `y = 3`, printing the results.

---

## 🟠 **Cell 2: Calculator Function**

Creates a **wrapper function** `calculator(x, y, operator)` that:

- Checks if the operator is valid.
- Routes to the correct arithmetic function based on the operator:
  - Handles `/`, `//`, `%` inside a `try` block (due to possible division by zero).
  - Handles `+`, `-`, `*`, `**` directly.
- Returns a **human-readable message** describing the operation result.

Then it runs **test calls** for each operator, again using `x = 5` and `y = 3`.

---

## 🟢 **Cell 3: Operator Dictionary + User Interaction**

Defines an `operators` dictionary that:

- Maps each operator symbol to its **name** and **layperson-friendly description**.

Then:

- Greets the user.
- Prompts the user to input two numbers.
- Lists all available operators with their descriptions.
- Prompts the user to **choose an operator**.
- Runs the `calculator()` function with the user’s inputs and prints the result.

---

## 💡 **Key Takeaways**

✅ Error handling for division by zero  
✅ Clear separation between low-level arithmetic functions and high-level calculator logic  
✅ Friendly user prompts and operator explanations  
✅ Good modular design for easy expansion later
