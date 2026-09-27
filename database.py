import json

def load_expenses():
    try:
        with open('expense.json', 'r') as file:
            expenses = json.load(file)
            return expenses
    except FileNotFoundError, json.JSONDecodeError:
        return {}

def save_expenses(expenses):
    with open('expense.json', 'w') as file:
        json.dump(expenses,file,indent=5)

