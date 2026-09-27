# Personal Expense Tracker

A web-based personal expense tracker built with Python and Flask. It allows users to add, view, update, delete, and search expenses while providing statistics and a visual breakdown of expenses by category.

## Features

* Add expenses
* Update existing expenses
* Delete expenses
* Search for expenses
* Expense validation
* Duplicate expense detection
* Expense statistics
* Category-based pie chart
* Success and error notifications with SweetAlert2
* JSON-based data storage
* Responsive dashboard
* Persistent data after restarting the application

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* Jinja2
* Chart.js
* SweetAlert2
* JSON

## Project Structure

```text
expense_tracker/
│
├── app.py
├── main.py
├── database.py
├── personal_expense_tracker.py
├── expense.json
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Collins-911/30_day_py_lock_in_roadmap.git
```

### 2. Navigate into the project

```bash
cd expense_tracker
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the application

```bash
python app.py
```

### 5. Open the application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## How It Works

The application uses Flask to handle web requests and Jinja2 to render the HTML pages.

Expense data is stored in `expense.json`. The application can create, read, update, and delete expense records from the JSON file.

The dashboard displays:

* Total amount spent
* Total number of expenses
* Number of expenses in each category
* A pie chart showing category distribution

## Expense Categories

The application currently supports:

* Food
* Transport
* Internet
* Other

## Future Improvements

Possible future improvements include:

* User authentication
* Database integration with SQLite or PostgreSQL
* Monthly expense reports
* Budget tracking
* More detailed charts
* Expense filtering by date
* Exporting expenses to CSV

## Author

**Collins Emelumba**

Built as a Python and Flask portfolio project.
