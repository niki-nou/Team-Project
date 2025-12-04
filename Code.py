# !pip install openai

import os

os.environ["OPENAI_API_KEY"]

import matplotlib.pyplot as plt
import numpy as np
from openai import OpenAI
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


#Getting inputs
overall_income = int(input("What is your monthly income? "))

rent = int(input("How much do you spend on rent per month? "))
utilities = int(input("How much do you spend on utilities per month? "))
food = int(input("How much do you spend on food per month? "))
insurance = int(input("How much do you spend on insurance per month? "))

total_expenses = rent + utilities + food + insurance
print("Your total expense is: " + str(total_expenses))

#Making inputs in a dictionary
expense_list = {
    "rent": rent,
    "ultilites": utilities,
    "food": food,
    "insurance": insurance
}

maximum = max(expense_list.values())
result = [key for key, value in expense_list.items() if value == maximum]

#Printing insights about the inputs
print("Your highest expense category is " + str(result))

necessities = overall_income - total_expenses
if necessities >= 0:
    print("You have $" + str(necessities) + " left over")
else:
    print("Your expenses is more than your income.")

#AI insights
prompt = f"""
Here is a user's monthly income and expenses:

Income: {overall_income}
Expenses: {expense_list}

Give them:
- A simple budget diagnosis
- One money saving tip
- Whether their expenses are good for someone with their income
"""

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [{"role": "user", "content": prompt}]
)

print(response.choices[0].message["content"])

#Expense breakdown with pie chart
plt.pie(expense_list.values(), labels=expense_list.keys(), autopct='%1.1f%%')
plt.title("Expense Breakdown")
plt.show()
# plt.xticks(range(len(expense_list)), list(expense_list.keys()))