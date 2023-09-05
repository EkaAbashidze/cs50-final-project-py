def main():
    financial_data = []
    data = get_info();
    print(data)
    


def get_info():
    expenses = int(input("How much was your expenses last month? "))
    income = int(input("What was your income last month? "))
    savings = int(input("How much savings did you make last month? "))
    return {"expenses": expenses, "income": income, "savings": savings};

def function_2():
    ...


def function_n():
    ...


if __name__ == "__main__":
    main()