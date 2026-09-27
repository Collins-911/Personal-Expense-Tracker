import  personal_expense_tracker

def main():
        def handle_operation():
            while True:
                while True:
                    user_option = input("===== Expense Tracker =====\n1 - Add Expense\n2 - View Expense\n3 - Search Expense\n4 - Update Expense\n5 - Delete Expense\n6 - View Statistics\n7 - Exit\nChoose an option: ")
                    if user_option == '1':
                        personal_expense_tracker.add_expense()
                    elif user_option == '2':
                        personal_expense_tracker.view_expenses()
                    elif user_option == '3':
                        personal_expense_tracker.search_expense()
                    elif user_option == '4':
                        personal_expense_tracker.update_expense()
                    elif user_option == '5':
                        personal_expense_tracker.delete_expense()
                    elif user_option == '6':
                        personal_expense_tracker.view_statistics()
                    elif user_option == '7':
                        personal_expense_tracker.exit_program()
                    else:
                        print(f'Invalid option - {user_option}')
                        continue
                    break
        handle_operation()

if __name__ == '__main__':
        main()

