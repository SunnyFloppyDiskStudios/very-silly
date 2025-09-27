"""
Challenge 5

Age Calculator
"""

from datetime import datetime

# input
dob_input = input("Enter your date of birth (dd/mm/yyyy): ")
dob = datetime.strptime(dob_input, "%d/%m/%Y")

today = datetime.now()

# calculation
days_lived = (today - dob).days

# Display
print(f"You have lived for {days_lived} days.")

# seconds
seconds_lived = (today - dob).total_seconds()
print(f"You have lived for {int(seconds_lived)} seconds.")
