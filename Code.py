!pip install openai

import os

# os.environ["OPENAI_API_KEY"]

import matplotlib.pyplot as plt
import numpy as np
from openai import OpenAI
# client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


#Getting inputs
overall_income = int(input("What is your monthly income? "))

rent = int(input("How much do you spend on rent per month? "))
utilities = int(input("How much do you spend on utilities per month? "))
food = int(input("How much do you spend on food per month? "))
insurance = int(input("How much do you spend on insurance per month? "))
other = int(input("How much do you spend on other expenses per month? "))

total_expenses = rent + utilities + food + insurance + other
savings = overall_income - total_expenses

#Making inputs in a dictionary
expense_list = {
    "rent": rent,
    "ultilites": utilities,
    "food": food,
    "insurance": insurance,
    "other": other
}

if savings > 0:
    expense_list["money left"] = savings

maximum = max(expense_list.values())
result = [key for key, value in expense_list.items() if value == maximum]



#Printing insights about the inputs
print("----------Your Budget Report----------")
print("Income: $" + str(overall_income))
print("Expenses: $" + str(total_expenses))
if savings < 0:
    print("You spent more than your income so you don't have any savings")
else:
    print("Money Left: $" + str(savings))
print("Your highest expense category is " + str(result))

print("\n--------------------------------------")


print("\nAI Recommendation")
#AI Insights
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("AI_TOKEN"),
)

completion = client.chat.completions.create(
    model="CohereLabs/c4ai-command-a-03-2025:cohere",
    messages=[
        {
            "role": "user",
            "content": f"""
            You are a financial advisor.
            Here is a user's monthly income and expenses:

            Income: {overall_income}
            Expenses: {expense_list}

            Give them:
            - A budget score out of 100
            - A recommendation on how to improve spending
            - One money saving tip
            - Whether their expenses are good for someone with their income
            Formatted as bullet points 
        """
        }
    ],
)

print(completion.choices[0].message.content)


#Expense breakdown with pie chart
plt.pie(expense_list.values(), labels=expense_list.keys(), autopct='%1.1f%%')
plt.title("Expense Breakdown")
plt.show()