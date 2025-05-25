monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

monthly_savings = monthly_income - monthly_expenses

projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_savings)


monthly_savings\s*=\s*(monthly_income\s*-\s*monthly_expenses|float\s*\(\s*monthly_income\s*\)\s*-\s*float\s*\(\s*monthly_expenses\s*\))


