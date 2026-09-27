import database
from datetime import datetime

expenses = database.load_expenses()

def create_expense(expense_name,expense_amount,expense_category):

    if expense_name in expenses:
        return False

    expense_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S:%p")

    expenses[expense_name] = {
        'amount' : expense_amount,
        'category' : expense_category,
        'date_time' : expense_time
    }

    database.save_expenses(expenses)
    return True

def add_expense():
    while True:
        # Name
        expense_name = input('Enter expense name: ').title().strip()
        if expense_name in expenses:
            print(f'Expense - {expense_name}, already exists!')
            continue
        break
        # Amount
    while True:
        try:
            expense_amount = float(input('Enter expense amount: ').strip())
        except ValueError:
            print('Amount must be a number!')
            continue
        if expense_amount < 0:
            print(f'Amount - {expense_amount}, cannot be less than zero!')
            continue
        break
        # Category
    while True:
        expense_category = input('1 - Food\n2 - Transport\n3 - Internet\n4 - Other\nChoose category: ').strip()
        if expense_category == '1':
            selected = 'Food'
        elif  expense_category == '2':
            selected = 'Transport'
        elif  expense_category == '3':
            selected = 'Internet'
        elif  expense_category == '4':
            selected = 'Other'
        else:
            print(f'Option - {expense_category}, is invalid!')
            continue
        break

    create_expense(expense_name,expense_amount,selected)
    print(f'Expense - {expense_name}, added succefully!')

def view_expenses():
    if not expenses:
        print('No expenses made!')
        return

    for name,details in expenses.items():
            print(f'==========\nName - {name}\nAmount - {details["amount"]}\nCategory: {details["category"]}\nTime Created - {details["date_time"]}')

def edit_expense(expense_name,expense_amount=None, expense_category=None):
    if expense_name not in expenses:
        return False

    if expense_amount is not None:
        expenses[expense_name]['amount'] = expense_amount

    if expense_category is not None:
        expenses[expense_name]['category'] = expense_category

    expenses[expense_name]['updated_date_time'] = datetime.now().strftime(
        "%d-%m-%Y %I:%M:%S:%p"
    )

    database.save_expenses(expenses)
    return True

def update_expense():

    if not expenses:
        print('No expenses made!')
        return

    while True:
        update_input = input('Enter expense name: ').title().strip()
        if update_input in expenses:
            choice_input = input('\n1 - Amount\n2 - Category\n3 - Exit\nChoose an option: ').strip()

            if choice_input == '1':
                while True:

                    try:
                        new_expense_amount = float(input('Enter new amount: ').strip())
                    except ValueError:
                        print('Amount must be a number!')
                        continue
                    if new_expense_amount < 0:
                        print(f'Amount - {new_expense_amount}, is less than zero!')
                        continue

                    expense_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S:%p")
                    expenses[update_input]['updated_date_time'] = expense_time
                    expenses[update_input]['amount'] = new_expense_amount
                    database.save_expenses(expenses)
                    print('Update successful!')
                    break

            elif choice_input == '2':
                while True:

                    new_expense_category = input('1 - Food\n2 - Transport\n3 - Internet\n4 - Other\nChoose category: ').strip()
                    if new_expense_category == '1':
                        selected = 'Food'
                    elif new_expense_category == '2':
                        selected = 'Transport'
                    elif new_expense_category == '3':
                        selected = 'Internet'
                    elif new_expense_category == '4':
                        selected = 'Other'
                    else:
                        print(f'Option - {new_expense_category}, is invalid!')
                        continue
                    expense_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S:%p")
                    expenses[update_input]['updated_date_time'] = expense_time
                    expenses[update_input]['category'] = selected
                    database.save_expenses(expenses)
                    print('Update successful!')
                    break

            elif choice_input == '3':
                print('Update cancelled!')
                return
            else:
                print(f'Invalid input - {choice_input}')
                continue
        else:
            print(f'Name - {update_input}, cannot be found!')
            continue

def remove_expense(expense_name):
    if expense_name in expenses:
        del expenses[expense_name]
        database.save_expenses(expenses)
        return True
    return False


def delete_expense():
    if not expenses:
        print('No expenses made!')
        return
    while True:
        expense_name = input('Enter expense name: ').strip().title()
        if remove_expense(expense_name):
            print(f'Expense - {expense_name}, deleted successfully!')
            break
        else:
            print(f'Name - {expense_name}, does not exist!')

def view_statistics():
    if not expenses:
        return None

    total = 0
    count = 0
    food_count = 0
    transport_count = 0
    internet_count = 0
    other_count = 0

    for name, details in expenses.items():
        total += details['amount']
        count += 1

        if details['category'] == 'Food':
            food_count += 1
        elif details['category'] == 'Transport':
            transport_count += 1
        elif details['category'] == 'Internet':
            internet_count += 1
        elif details['category'] == 'Other':
            other_count += 1

    return {
        'total': total,
        'count': count,
        'Food': food_count,
        'Transport': transport_count,
        'Internet': internet_count,
        'Other': other_count
    }

stats = view_statistics()

if stats is None:
    print('No expenses made!')
else:
    print(
        f"\nTotal amount - ₦{stats['total']}"
        f"\nFood - {stats['Food']}"
        f"\nTransport - {stats['Transport']}"
        f"\nInternet - {stats['Internet']}"
        f"\nOther - {stats['Other']}"
        f"\nTotal count - {stats['count']}"
    )


def search_expense():
    if not expenses:
        print('No expenses made!')
    while True:
        search = input('Enter expense name: ').strip().title()
        if search in expenses:
            for name,details in expenses.items():
                if name == search:
                    print(f'Name - {name}\nAmount - {details['amount']}\nCategory - {details['category']}\nDate and Time - {details['date_time']}')
        else:
            print(f'Name - {search}, does not exist!')
            continue
        break

def find_expense(expense_name):
    if expense_name in expenses:
        return expenses[expense_name]
    else:
        return None

def exit_program():
    print('Goodbye!')
    exit()


















