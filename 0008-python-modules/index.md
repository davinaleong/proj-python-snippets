# 📘 Davina's Calculator — Layperson Explanation

This notebook explains the code behind **Davina's Calculator**, written in Python.  
The calculator allows you to input two numbers, pick an arithmetic operation, and get a result.

---

## 💡 What does the code do?

Let’s break it down step by step:

---

### 1️⃣ Import all calculator functions

```python
from calculator import *
```

✅ This line brings in all the **calculation functions** (like `add`, `subtract`, `multiply`) from another file called `calculator.py` so we can use them here.

---

### 2️⃣ Print a welcome message

```python
print("== Welcome to Davina's Calculator ==")
```

✅ Displays a friendly message so the user knows they’ve opened the calculator program.

---

### 3️⃣ Get two numbers from the user

```python
x = float(input("Please give a number (decimals and negative numbers are allowed):"))
y = float(input("Please give another number (decimals and negative numbers are allowed):"))
```

✅ Asks the user to **type in two numbers**, which can include decimals (like 3.5) or negatives (like -2).

✅ Converts the typed input into **floating-point numbers** (numbers with decimals).

---

### 4️⃣ Show the list of available operations

```python
print("Here are the available arithmetic operators:")
for op_symbol, op_info in operators.items():
    name = op_info["name"]
    description = op_info["description"]
    print(f"\t'{op_symbol}' - {name}: {description}")
```

✅ Goes through a dictionary called `operators` that lists:

- The **symbol** (like `+` or `*`)
- The **name** (like "Add" or "Multiply")
- A **short description** (explaining what it does)

✅ Prints this neatly so the user can see all the choices.

---

### 5️⃣ Ask the user to choose an operation

```python
operator = input("Choose one:")
```

✅ Waits for the user to type in an **operator symbol** (like `+`, `-`, `*`, `/`, etc.).

---

### 6️⃣ Calculate and display the result

```python
print(calculator(x, y, operator))
```

✅ Calls the `calculator()` function (defined elsewhere) to:

- Perform the selected calculation (like adding, subtracting, dividing)
- Generate a message with the result

✅ Prints the final answer for the user.

---

## 🎯 Summary for Non-Coders

In short, this program:
✅ Greets you
✅ Asks for two numbers
✅ Shows you math options
✅ Lets you pick one
✅ Gives you the answer

All automatically — like a simple text-based calculator!
