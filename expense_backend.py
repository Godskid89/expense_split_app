import pandas as pd
from collections import defaultdict

def read_expenses(file_path):
    try:
        return pd.read_excel(file_path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Description", "Paid By", "Participants"])

def add_expense(file_path, data):
    df = read_expenses(file_path)
    df = df.append(data, ignore_index=True)
    df.to_excel(file_path, index=False)

def delete_expense(file_path, index):
    df = read_expenses(file_path)
    df = df.drop(index)
    df.to_excel(file_path, index=False)

def update_expense(file_path, index, data):
    df = read_expenses(file_path)
    df.loc[index] = data
    df.to_excel(file_path, index=False)

def calculate_debts(file_path):
    df = read_expenses(file_path)
    debts = defaultdict(float)

    for _, row in df.iterrows():
        participants = row["Participants"].split(',')
        amount_per_person = row["Amount"] / len(participants)
        for person in participants:
            person = person.strip()
            if person != row["Paid By"]:
                debts[person] += amount_per_person
    
    return debts

def monthly_summary(file_path):
    df = read_expenses(file_path)
    df['Month'] = pd.to_datetime(df['Date']).dt.to_period('M')
    summary = df.groupby(['Month', 'Category']).sum()['Amount']
    return summary
