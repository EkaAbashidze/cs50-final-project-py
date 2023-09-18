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


# def test_get_percentages():
#     ...


# def test_calculate_net_income():
#     ...