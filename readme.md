# Expense Slip App

## Project Overview

The Expense Slip App is a Python-based application designed to manage and track expenses. It uses Streamlit for the frontend and an Excel file as the backend database. The app allows users to add, view, and manage their expenses, visualize debts and monthly expense summaries through charts.

## Features

- **Add Expenses**: Users can add new expenses with details like date, category, amount, description, payer, and participants.
- **View Expenses**: Display a list of all recorded expenses.
- **Debt Calculation**: Calculates and displays how much each participant owes.
- **Monthly Summary**: Shows a summary of expenses for each month.
- **Data Visualization**: Includes pie charts for debts and bar charts for monthly expense summaries.

## Installation

Before running the app, ensure you have Python installed on your system. Then, install the necessary dependencies:

```bash
pip install streamlit pandas openpyxl matplotlib plotly
```

## Running the Application

To run the app, navigate to the project directory in your terminal and execute the following command:

```bash
streamlit run app.py
```

## File Structure

- `app.py`: Contains the Streamlit frontend code.
- `expense_backend.py`: Handles the backend operations like reading and writing to the Excel file, and calculating debts and summaries.

## How to Use

1. **Start the App**: Run the app using the above command.
2. **Add an Expense**: Fill in the form with the expense details and submit.
3. **View Expenses**: Scroll through the list of expenses.
4. **Visualize Data**: Check the pie and bar charts for a visual representation of debts and monthly expenses.


## Contact

[JOSEPH OLADOKUN] - [jossy@iastate.edu]
[ERIC ASARE] - [ejasare@iastate.edu]

Project Link: [GitHub Repository Link, if available]

