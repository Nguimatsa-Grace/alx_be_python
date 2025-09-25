def perform_operation(num1, num2, operation):
    """
    Performs a basic arithmetic operation on two numbers.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float or str: The result of the operation, or an error message for division by zero.
    """
    # Use a match-case statement to perform the correct operation.
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            # Handle division by zero.
            if num2 == 0:
                return "Division by zero is not allowed."
            return num1 / num2
        case _:
            # Return an error message for an invalid operation.
            return "Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."
