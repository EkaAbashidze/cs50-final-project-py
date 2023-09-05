import matplotlib.pyplot as plt
from asciichartpy import plot

def main():
    financial_data = get_info();
    print(financial_data)
    get_percentages(financial_data)

def get_info():
    income = int(input("How much was your income last month? "))
    expenses = int(input("How much expenses did you have last month? "))
    savings = int(input("How much savings did you make last month? "))
    return {"expenses": expenses, "income": income, "savings": savings};

def get_percentages(data):
    total_expenses = data["expenses"]
    total_income = data["income"]
    total_savings = data["savings"]
    
    expense_percentage = (total_expenses / total_income) * 100
    savings_percentage = (total_savings / total_income) * 100
    
    print("\nFinancial Percentages:")
    print(f"Expense Percentage: {expense_percentage}%")
    print(f"Savings Percentage: {savings_percentage}%")


def function_n():
    ...


if __name__ == "__main__":
    main()