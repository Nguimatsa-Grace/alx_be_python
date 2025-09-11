# finance_calculator.py

# Prompt user for monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt user for monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Annual interest rate
interest_rate = 0.05

# Project savings after one year with interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * interest_rate)

# Display results
print("Your monthly savings are:", monthly_savings)
print("Your projected savings after one year (with interest) are:", projected_savings)
