from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in a specific format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Calculates a future date by adding a user-specified number of days.
    """
    try:
        days_to_add_str = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_to_add_str)
        
        # Get the current date and add the specified number of days
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        
        # Format and print the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")

    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
