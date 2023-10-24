import pytest
from meals import Day, InvalidInputError
from recipes import get_recipes

# Test set_meals
def test_set_meal_calories():
    calorie_targets = [1500, 1850, 2150, 2400, 2800, 3000]
    expected_calories = [
        {"M1": 350, "M2": 350, "M3": 500, "M4": 150, "M5": 200},
        {"M1": 400, "M2": 400, "M3": 600, "M4": 300, "M5": 200},
        {"M1": 500, "M2": 500, "M3": 600, "M4": 400, "M5": 300},
        {"M1": 500, "M2": 600, "M3": 700, "M4": 400, "M5": 400},
        {"M1": 600, "M2": 650, "M3": 800, "M4": 500, "M5": 400},
        {"M1": 600, "M2": 650, "M3": 800, "M4": 500, "M5": 400},
    ]

    # Iterate through the calorie targets
    for i in range(len(calorie_targets)):
        # Set day object with the calorie target specified
        day = Day(calorie_target=calorie_targets[i])
        # Run set_meal_calories function
        day.set_meal_calories()
        # Check expected calories match
        assert day.meal_calories == expected_calories[i]

# Test shuffle_recipes
def test_shuffle_recipes():
    original_list = get_recipes()
    shuffled_list = Day.shuffle_recipes
    assert original_list != shuffled_list

# Test check_calorie_change
def test_check_calorie_change_y():
    day = Day(calorie_target=1800)
    assert day.check_calorie_change('y') is True

def test_check_calorie_change_n():
    day = Day(calorie_target=1800)
    assert day.check_calorie_change('n') is False
