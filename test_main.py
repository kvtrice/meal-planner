import main
import pytest
from meals import InvalidInputError

# Test Get Calorie Target with valid input
def test_get_calorie_target_valid():
    result = main.get_calorie_target("1700")
    assert result == 1700

# Test get_calorie_target with out of range input
def test_get_calorie_target_invalid_range():
    with pytest.raises(InvalidInputError):
        main.get_calorie_target("1300")

# Test get_calorie_target with invalid type (string)
def test_get_calorie_target_invalid_type():
    with pytest.raises(InvalidInputError):
        main.get_calorie_target("hello")

# Test get_num_days function with valid input
def test_get_num_days_valid_input():
    result = main.get_num_days("7")
    assert result == 7

# Test get_num_days function with out of range number
def test_get_num_days_invalid_input():
    with pytest.raises(InvalidInputError):
        main.get_num_days("20")

# Test get_num_days function with invalid type (string)
def test_get_num_days_invalid_input():
    with pytest.raises(InvalidInputError):
        main.get_num_days("20")