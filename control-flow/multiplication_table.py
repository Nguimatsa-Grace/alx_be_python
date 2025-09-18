# This script generates a multiplication table for a number provided by the user.

# 1. Prompt the user for a number and convert the input to an integer.
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# 2. Use a for loop to iterate from 1 to 10.
# The range function generates numbers from the start value up to, but not including, the stop value.
# So, range(1, 11) will generate numbers from 1 to 10.
print()  # Add an empty line for better formatting
for i in range(1, 11):
    # 3. Calculate the product for each iteration.
    product = number * i
    
    # 4. Print the result in the specified format: "X * Y = Z".
    print(f"{number} * {i} = {product}")
