# import necessary modules
import math

# Programmer Input
amount_borrowed = 270000
interest_rate = 0.05125
payback_period = 30

# Logic
months = 12 * payback_period
interest_rate_month = interest_rate / 12 # Divided by 12 for each month
interest_rate_formatted = "%.3f" % (interest_rate * 100)
calc_monthly_payment = (amount_borrowed * pow(1 + interest_rate_month, months) * interest_rate_month) / (pow(1 + interest_rate_month, months) - 1)
calc_monthly_payment_formatted = "%.2f" % calc_monthly_payment

# Output
print("Amount borrowed = $", amount_borrowed, sep = "", end = "\n\n")
print("Annual interest rate = ", interest_rate_formatted, "%", sep = "", end = "\n\n")
print("Payback period = ", payback_period, " Years", sep = "", end = "\n\n")
print("Monthly payment = $", calc_monthly_payment_formatted, sep = "", end = "\n\n")

# Notes
# amount_borrowed = input("Enter amount borrowed: ")
# interest_rate = input("Enter interest rate: ")
# payback_period = input("Enter interest rate: ")
# print("This is the amount borrowed", amount_borrowed)
# print("Enter interest rate: ")
# print("Enter 30 year payback period: ")
# print(amount_borrowed)
# dollar amount to be borrowed (whole number)
# Annual percent interest rate (floating point number)
# Calculate the monthly payment in dollars, (floating-point number)
# Include in the output an echo of the input amount borrowed,
# the annual percent interest rate (without formatting) and the payback period (in years).
# Include in the output the calculated monthly payment,
# formatted to show two decimal places (like this: 1000.00)

