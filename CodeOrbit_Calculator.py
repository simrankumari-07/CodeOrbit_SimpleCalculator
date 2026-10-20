# Simple Calculator
# This program performs basic arithmetic operations.

# Display the calculator title
print("===== SIMPLE CALCULATOR =====")

try:
    # Get the first number from the user
    num1 = float(input("Enter first number: "))

    # Get the arithmetic operator from the user
    operator = input("Enter operator (+, -, *, /): ")

    # Get the second number from the user
    num2 = float(input("Enter second number: "))

    # Perform addition
    if operator == "+":
        print("Result:", num1 + num2)

    # Perform subtraction
    elif operator == "-":
        print("Result:", num1 - num2)

    # Perform multiplication
    elif operator == "*":
        print("Result:", num1 * num2)

    # Perform division
    elif operator == "/":
        # Check whether the second number is zero
        if num2 != 0:
            print("Result:", num1 / num2)
        # Prevent division by zero
        else:
            print("Error: Cannot divide by zero!")

    # Handle an invalid operator
    else:
        print("Invalid operator!")

# Handle invalid number inputs
except ValueError:
    print("Error: Please enter valid numbers!")
