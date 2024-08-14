# Function to perform the selected arithmetic operation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

# Prompt user for input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ").strip()

    # Perform calculation and display result
    result = calculate(num1, num2, operation)
    print(f"The result of {num1} {operation} {num2} is: {result}")

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
