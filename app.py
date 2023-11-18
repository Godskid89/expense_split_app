import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import date
from expense_backend import add_expense, read_expenses, delete_expense, update_expense, calculate_debts, monthly_summary

st.title('Hello, Everyone!')

st.write('This is the project for MIS 532')

def show_expense_form():
    with st.form("expense_form"):
        exp_date = st.date_input("Date", date.today())
        exp_category = st.text_input("Category")
        exp_amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        exp_description = st.text_area("Description")
        exp_paid_by = st.text_input("Paid By")
        exp_participants = st.text_input("Participants (comma-separated)")
        submit_action = st.form_submit_button("Submit")

        if submit_action:
            return {
                "Date": exp_date, 
                "Category": exp_category, 
                "Amount": exp_amount, 
                "Description": exp_description, 
                "Paid By": exp_paid_by, 
                "Participants": exp_participants
            }
    return None

st.title('Expense Slip App')

# Expense form
new_expense_data = show_expense_form()
if new_expense_data:
    add_expense("expenses.xlsx", new_expense_data)
    st.success("Expense added successfully!")

# Display existing expenses
st.subheader("Existing Expenses")
df = read_expenses("expenses.xlsx")
st.dataframe(df)

# Display debts and a pie chart for visualization
st.subheader("Debts")
debts = calculate_debts("expenses.xlsx")
debt_names = list(debts.keys())
debt_amounts = list(debts.values())

if debt_names:
    fig, ax = plt.subplots()
    ax.pie(debt_amounts, labels=debt_names, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

# Display monthly summary and a bar chart
st.subheader("Monthly Summary")
summary = monthly_summary("expenses.xlsx")
st.write(summary)

if not summary.empty:
    summary_df = summary.reset_index()
    summary_df['Month'] = summary_df['Month'].astype(str)
    fig = px.bar(summary_df, x='Month', y='Amount', color='Category', barmode='group')
    st.plotly_chart(fig)
