# This script provides a personal daily reminder based on user input for a single task.

# 1. Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# 2. Process the task based on priority and time sensitivity
reminder = ""

match priority:
    case 'high' | 'High':
        reminder = f"'{task}' is a high priority task"
    case 'medium' | 'Medium':
        reminder = f"'{task}' is a medium priority task"
    case 'low' | 'Low':
        reminder = f"'{task}' is a low priority task"
    case _:
        # Handle invalid priority input
        print("Invalid priority entered. Please choose from high, medium, or low.")
        # Exit the script to prevent further execution with invalid data
        exit()

# 3. Add a time-sensitive clause if applicable
if time_bound == 'yes':
    reminder += " that requires immediate attention today!"
else:
    # Add a note for non-time-bound tasks, ensuring the format is correct
    if priority == 'low' or priority == 'Low':
        reminder = f"Note: {reminder}. Consider completing it when you have free time."
    else:
        # For non-time-bound, non-low priority tasks, add a general completion note.
        reminder += ". Consider completing it soon."

# 4. Print the final customized reminder
print("Reminder:", reminder)



