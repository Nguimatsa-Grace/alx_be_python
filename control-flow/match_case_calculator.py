def get_user_input():
    """Prompts the user to enter two numbers and an operation."""
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose the operation (+, -, *, /): ")
        return num1, num2, operation
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None, None, None

def perform_calculation(num1, num2, operation):
    """Performs the calculation based on the selected operation."""
    result = None
    message = ""

    match operation:
        case '+':
            result = num1 + num2
            message = f"The result is {result}."
        case '-':
            result = num1 - num2
            message = f"The result is {result}."
        case '*':
            result = num1 * num2
            message = f"The result is {result}."
        case '/':
            # Handle division by zero gracefully
            if num2 != 0:
                result = num1 / num2
                message = f"The result is {result}."
            else:
                message = "Cannot divide by zero."
        case _:
            # Handle unexpected operation input
            message = "Invalid operation. Please choose from +, -, *, /."

    print(message)

# Main part of the script
if __name__ == "__main__":
    n1, n2, op = get_user_input()
    if n1 is not None and n2 is not None and op is not None:
        perform_calculation(n1, n2, op)
