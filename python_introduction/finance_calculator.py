# A python script to calculate the user’s monthly savings based on inputted monthly income and expenses.
# It will then project these savings over a year, assuming a fixed interest rate, 
# to demonstrate compound interest’s effect on savings.

# User Input for Financial Details:
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings:
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings:
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

# Output Result:
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
