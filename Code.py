import matplotlib.pyplot as plt
import numpy as np


overall_income = int(input("What is your monthly income? "))

rent = int(input("How much do you spend on rent per month? "))
utilities = int(input("How much do you spend on utilities per month? "))
food = int(input("How much do you spend on food per month? "))
insurance = int(input("How much do you spend on insurance per month? "))

total_expenses = rent + utilities + food + insurance

print("Your total expense is: " + str(total_expenses))
expense_list = {
    "rent": rent,
    "ultilites": utilities,
    "food": food,
    "insurance": insurance
}

maximum = max(expense_list.values())
result = [key for key, value in expense_list.items() if value == maximum]

print("Your highest expense category is " + str(result))

necessities = overall_income - total_expenses
if necessities >= 0:
    print("You have $" + str(necessities) + " left over")
else:
    print("Your expenses is more than your income.")

