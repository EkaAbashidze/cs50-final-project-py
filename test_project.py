from project import get_info
from project import get_percentages
from project import calculate_net_income

def test_get_info():
    data = get_info()
    assert "income" in data 
    assert isinstance(data["income"], int)
    assert "income" in data 
    assert isinstance(data["income"], int)
    assert "expenses" in data 
    assert isinstance(data["expenses"], int)
    assert "savings" in data 
    assert isinstance(data["savings"], int)


def test_get_percentages():
    data = {"income": 1000, "expenses": 300, "savings": 200}

    expected_expense_percentage = (data["expenses"] / data["income"] * 100)
    expected_savings_percentage = (data["savings"] / data["income"] * 100)
    
    assert expected_expense_percentage == 30
    assert expected_savings_percentage == 20

def test_calculate_net_income():
    data = {"income": 1000, "expenses": 300}
    
    expected_net_income = data["income"] - data["expenses"]
    
    assert expected_net_income == 700