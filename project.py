def main():
    financial_data = get_info();
    print(financial_data)
    get_percentages(financial_data)
    calculate_net_income(financial_data)

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


def calculate_net_income(data):
    total_income = data["income"]
    total_expenses = data["expenses"]
    
    net_income = total_income - total_expenses
    
    print("\nFinancial Summary:")
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Net Income: ${net_income}")


if __name__ == "__main__":
    main()