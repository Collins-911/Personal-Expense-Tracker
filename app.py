from flask import Flask, render_template, request, redirect, url_for, flash
import database
from personal_expense_tracker import (
    create_expense,
    remove_expense,
    edit_expense,
    view_statistics,
    find_expense
)

VALID_CATEGORIES = ['Food', 'Transport', 'Internet', 'Other']
app = Flask(__name__)
app.secret_key = 'my-expense-tracker-secret-key'


@app.route('/')
def home():
    expenses = database.load_expenses()
    stats = view_statistics()
    return render_template('index.html', expenses=expenses, stats=stats)


@app.route('/add', methods=['POST'])
def add_expense():
    name = request.form.get('name')

    if not name:
        flash('Name required!', 'error')
        return redirect(url_for('home'))

    name = name.title()

    try:
        amount = float(request.form.get('amount'))
    except (TypeError, ValueError):
        flash('Invalid amount!', 'error')
        return redirect(url_for('home'))

    if amount <= 0:
        flash(f'Amount must be greater than zero - {amount}', 'error')
        return redirect(url_for('home'))

    category = request.form.get('category')


    if category not in VALID_CATEGORIES:
        flash(f'Invalid category - {category}', 'error')
        return redirect(url_for('home'))

    success = create_expense(name, amount, category)

    if not success:
        flash('Expense already exists!', 'error')
        return redirect(url_for('home'))

    flash('Expense added successfully!', 'success')
    return redirect(url_for('home'))


@app.route('/delete/<name>', methods=['POST'])
def delete_expense(name):
    success = remove_expense(name)

    if success:
        flash('Expense deleted successfully!', 'success')
    else:
        flash('Expense not found!', 'error')

    return redirect(url_for('home'))


@app.route('/update/<name>', methods=['POST'])
def update_expense(name):
    try:
        amount = float(request.form.get('amount'))
    except (ValueError, TypeError):
        flash('Invalid amount!', 'error')
        return redirect(url_for('home'))

    if amount <= 0:
        flash(f'Amount must be greater than zero - {amount}', 'error')
        return redirect(url_for('home'))

    category = request.form.get('category')

    if category not in VALID_CATEGORIES:
        flash(f'Invalid category - {category}', 'error')
        return redirect(url_for('home'))

    success = edit_expense(name, amount, category)

    if success:
        flash('Expense updated successfully!', 'success')
    else:
        flash('Expense not found!', 'error')

    return redirect(url_for('home'))


@app.route('/search', methods=['GET'])
def search_expense():
    name = request.args.get('name')

    if not name:
        flash('Name required!', 'error')
        return redirect(url_for('home'))

    name = name.title()

    result = find_expense(name)

    if not result:
        flash(f'Expense "{name}" was not found!', 'error')

    return render_template(
        'index.html',
        expenses=database.load_expenses(),
        stats=view_statistics(),
        search_result=result,
        search_name=name
    )


if __name__ == '__main__':
    app.run(debug=True)