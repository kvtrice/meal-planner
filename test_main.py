import main
import pytest
from io import StringIO

# Test Get Calorie Target with valid inputs
def test_get_calorie_target_valid(monkeypatch):
    input_data = StringIO('1400\n2100\n3000\n')
    monkeypatch.setattr('sys.stdin', input_data)

    expected_values = [1400, 2100, 3000]

    for expected_value in expected_values:
        actual_value = main.get_calorie_target()
        assert actual_value == expected_value



# Test get_num_days function with valid input
def test_get_num_days_valid_input():
    result = main.get_num_days("7")
    assert result == 7

# Test get_num_days function with invalid input
def test_get_num_days_invalid_input():
    with pytest.raises(ValueError):
        main.get_num_days("20")