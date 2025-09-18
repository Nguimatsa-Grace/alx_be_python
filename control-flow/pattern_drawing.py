# This script draws a square pattern of asterisks based on user input.

# 1. Prompt the user for a positive integer for the pattern size.
try:
    size = int(input("Enter the size of the pattern: "))
    # Ensure the input is a positive integer
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# 2. Use a while loop to iterate through each row.
row = 0
while row < size:
    # 3. Inside the while loop, use a for loop for each column.
    for col in range(size):
        # 4. Print an asterisk without a newline.
        print("*", end="")
    
    # 5. Print a newline character to move to the next row.
    print()
    
    # 6. Increment the row counter for the while loop.
    row += 1
