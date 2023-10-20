import random
from user_plan import User
from recipes import get_recipes

# Define day Class --> Will ecentually have multiple day objects creating a full weeks worth of meals


class Day():
    def __init__(self, calorie_range, daily_calories):
        # Empty dictionary to store the calorie target for each meal (based on the calorie range we determined from the users total daily calories)
        # This will be 5 objects with a calorie range that will be iterated over
        self.calorie_range = calorie_range
        self.daily_calories = daily_calories
        self.meal_calories = {}

        # Set the meal calories (based on the calorie range) each time a day is initialized
        self.set_meal_calories(self.calorie_range)

        # Empty list to store all the meals for the day
        # Will iterate over the meal_calories dictionary and for each meal find a meal from the recipes list that is within that range
        # Each of those meals will be added into this list
        # This list will eventually contain 5 meals for the day
        self.todays_meals = []

    def __repr__(self):
        return f"Daily Calorie Target is: {self.daily_calories}\nCalorie Range is: {self.calorie_range}\nMeal Calories are: {self.meal_calories}\n Today's Meals are: {self.todays_meals}"

    # Function to set the calories required for each meal in order for the user to get meals that match their specific calorie range for the day
    def set_meal_calories(self, calorie_range):
        # Based on each calorie_range, set the dictionary to equal the below specified calories
        match calorie_range:

            # For 1400 - 1700 Cals ->
            case 1:
                self.meal_calories = {
                    "M1": 400,
                    "M2": 400,
                    "M3": 500,
                    "M4": 250,
                    "M5": 200,
                }
            # For 1701 - 2000 Cals ->
            case 2:
                self.meal_calories = {
                    "M1": 400,
                    "M2": 400,
                    "M3": 600,
                    "M4": 300,
                    "M5": 200,
                }
            # For 2001 - 2300 Cals ->
            case 3:
                self.meal_calories = {
                    "M1": 500,
                    "M2": 500,
                    "M3": 600,
                    "M4": 400,
                    "M5": 300,
                }
            # For 2301 - 2600 Cals ->
            case 4:
                self.meal_calories = {
                    "M1": 500,
                    "M2": 600,
                    "M3": 700,
                    "M4": 400,
                    "M5": 400,
                }
            # For 2601 - 3000 Cals ->
            case 5:
                self.meal_calories = {
                    "M1": 600,
                    "M2": 650,
                    "M3": 800,
                    "M4": 500,
                    "M5": 400,
                }

    # Function to find and select meals for the specified calorie_ranges
    def set_meals(self):
        # Get all recipes (as a dictionary)
        get_recipes()

        # While todays meals is incomplete
        while True:
        # For each of the meals (meal1, meal2 etc.)
            for calories in self.meal_calories.values():
                # For the value in that dict (cals), +- 75 either side
                min_cal = calories - 75
                max_cal = calories + 75
                meal_found = False

                print(f"Calorie Range Min: {min_cal} cals, Max is {max_cal} cals")

                # Iterate over the recipes to find a meal, and check it's in the calorie range. While it's not, keep searching, if it is, add it to today's meals and set meal_found to True
                while meal_found == False:
                    pass

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