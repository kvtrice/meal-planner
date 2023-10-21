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

    # def __repr__(self):

    #     for item in self.todays_meals:
    #         return f"Daily Calorie Target is: {self.daily_calories}\nCalorie Range is: {self.calorie_range}\nMeal Calories are: {self.meal_calories}"

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
        
        attempts = 0
        # Get all recipes (as a dictionary)
        recipes = get_recipes()
        # Shuffle recipes so it's a random one being returned
        random.shuffle(recipes)

        meal_completed = False
        # While todays meals is incomplete
        while meal_completed == False and attempts < 100:
        # For each of the meals (meal1, meal2 etc.)
            for calories in self.meal_calories.values():
                # For the value in that dict (cals), +- 75 either side
                min_cal = calories - 75
                max_cal = calories + 75
                meal_found = False

                # Iterate over the recipes to find a meal, and check it's in the calorie range. While it's not, keep searching, if it is, add it to today's meals and set meal_found to True
                while meal_found == False:
                    # Iterate through the recipes list of dictionaries
                    for recipe in recipes:
                        # Find the 'calories' value
                        value = int(recipe.get('calories'))
                        # Check if that value is within the meals acceptable range
                        if min_cal < value < max_cal:
                            # If it is, append it to todays meals
                            self.todays_meals.append(recipe)
                            # Remove from the recipe list (so as to not duplicate on the same day)
                            recipes.remove(recipe)
                            meal_found = True
                            # Exit the loop
                            break

                    if meal_found == False:
                        meal_found = True
                        raise Exception("Sorry, we couldn't find a recipe for this meal.")
            
            # Check that meal total is acceptable close to the users target calories
            total_calories = 0
            # Sum each meals calories together to find the total
            for meal in self.todays_meals:
                total_calories += int(meal['calories'])
            
            # Set the range to be acceptable based on the daily calories goal
            daily_min_cal = self.daily_calories - 75
            daily_max_cal = self.daily_calories + 75

            # If within target, mark meal as completed
            if daily_min_cal < total_calories < daily_max_cal:
                meal_completed = True
            # Otherwise, start again
            else:
                self.todays_meals = []
                recipes = get_recipes()
                random.shuffle(recipes)
                attempts += 1

        if attempts >= 100:
            raise Exception("Sorry, we were unable to find a suitable meal plan for you at this time. Please try again with a different calorie target or add some more recipes.")

    # Function to print the days meal plan once it's been set
    def print_daily_meal(self):
        total_calories = 0
        print(f"\nBased on your daily calorie goal, here is today's meals:\n")

        semantic_meal_names = ["Breakfast", "Lunch", "Dinner", "Snack 1", "Snack 2"]

        for meal_name, semantic_name in zip(self.todays_meals, semantic_meal_names):
            total_calories += int(meal_name['calories'])
            print(f"{semantic_name}: {meal_name['title']} ({meal_name['calories']} calories) ")
            print(f"Ingredients: {meal_name['ingredients']}\n ")
        
        print(f"\nThe total calories for the day is: {total_calories}\n")

