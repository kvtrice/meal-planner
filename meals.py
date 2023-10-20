import random
from user_plan import User


class Day():
    def __init__(self, daily_calories, calorie_range):
        self.meal_calories = {}
        self.get_meal_calories(calorie_range)
        self.todays_meals = []
    
    def set_meal_calories(self, calorie_range):
        match calorie_range:
            case 1:
                self.meal_calories = {
                    "M1" : 250,
                    "M2" : 250,
                    "M3" : 250,
                    "M4" : 250,
                    "M5" : 250,
                }
            case 2:
                self.meal_calories = {
                    "M1" : 250,
                    "M2" : 250,
                    "M3" : 250,
                    "M4" : 250,
                    "M5" : 250,
                }
            case 3:
                self.meal_calories = {
                    "M1" : 250,
                    "M2" : 250,
                    "M3" : 250,
                    "M4" : 250,
                    "M5" : 250,
                }
            case 4:
                self.meal_calories = {
                    "M1" : 250,
                    "M2" : 250,
                    "M3" : 250,
                    "M4" : 250,
                    "M5" : 250,
                }
            case 5:
                self.meal_calories = {
                    "M1" : 250,
                    "M2" : 250,
                    "M3" : 250,
                    "M4" : 250,
                    "M5" : 250,
                }

    def set_meals(self):
        pass
        # Load the latest recipes into a dictionary
        # WHILE (complete == false):
        #   Loop (run 5 times):
        #       For each Meal calorie mid-point, set the range to be +- 100   (based on the value of that key)
        #       Search the recipe dictionary for a meal that matches the range we gave
        #       Find all recipes that match the range - add to a new dictionary
        #       randomChoice function from Random on that dictionary
        #       Add that random choice (dictionary) to self.todays_meals (list)
        #   Loop:
        #       Sum the values of each dictionary in the list
        #   If within +/- 50 of initial daily calorie intake goal
                # Set complete to TRUE

