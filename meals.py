import random
from recipes import get_recipes
from main import InvalidInputError

# ----------------------------------------------------------------

class FindRecipeError(Exception):
    pass

class Day():
    def __init__(self, calorie_target):
        self.calorie_target = calorie_target
        self.meal_calories = {}  # Store meal calories based on the users calorie target
        # Set the meal calories (based on the calorie range) each time a day is initialized
        self.set_meal_calories()
        self.todays_meals = []  # Empty list for todays meals
        self.day_result = None

    # Set the calories required for each meal based on user calorie target
    def set_meal_calories(self):
        # Based on each calorie_range, set the dictionary to equal the below specified calories
        if 1400 <= self.calorie_target <= 1700:
            self.meal_calories = {
                "M1": 350,
                "M2": 350,
                "M3": 500,
                "M4": 150,
                "M5": 200,
            }
        elif 1701 <= self.calorie_target <= 2000:
            self.meal_calories = {
                "M1": 400,
                "M2": 400,
                "M3": 600,
                "M4": 300,
                "M5": 200,
            }
        elif 2001 <= self.calorie_target <= 2300:
            self.meal_calories = {
                "M1": 500,
                "M2": 500,
                "M3": 600,
                "M4": 400,
                "M5": 300,
            }
        elif 2301 <= self.calorie_target <= 2600:
            self.meal_calories = {
                "M1": 500,
                "M2": 600,
                "M3": 700,
                "M4": 400,
                "M5": 400,
            }
        elif 2601 <= self.calorie_target <= 3000:
            self.meal_calories = {
                "M1": 600,
                "M2": 650,
                "M3": 800,
                "M4": 500,
                "M5": 400,
            }


    def shuffle_recipes(self):
        recipe_list = get_recipes()  # Get all recipes (as a dictionary)
        # Shuffle recipes so it's a random one being returned
        random.shuffle(recipe_list)
        return recipe_list


    # Function to find and select meals for the specified calorie_ranges
    def set_meals(self):
        attempts = 0  # Num of attempts to set a valid meal plan
        meal_completed = False
        recipes = self.shuffle_recipes()

        # While todays meals is incomplete
        while meal_completed == False and attempts < 1000:
            for calories in self.meal_calories.values():
                # For the value in that dict (cals), +- 75 either side
                min_cal = calories - 75
                max_cal = calories + 75
                meal_found = False

                # Iterate over the recipes to find a meal, and check it's in the calorie range.
                # While it's not, keep searching, if it is, add it to today's meals and set meal_found to True
                while meal_found == False:
                    for recipe in recipes:
                        # Find the 'calories' value
                        value = int(recipe.get('calories'))
                        if min_cal < value < max_cal:  # Check value within acceptable range
                            # Append to todays meals
                            self.todays_meals.append(recipe)
                            # Remove from the recipe list (so as to not duplicate on the same day)
                            recipes.remove(recipe)
                            meal_found = True
                            break  # Exit the loop

                    if meal_found == False:
                        meal_found = True
                        raise FindRecipeError("Sorry, we were unable to find a suitable meal for you with the current calorie target and available recipes. Please consider one of the following options:\n1. Adjust your daily calorie target to a different target.\n2. Add more recipes to your collection.")

            # Check that meal total is acceptable close to the users target calories
            total_calories = 0
            # Sum each meals calories together to find the total
            for meal in self.todays_meals:
                total_calories += int(meal['calories'])

            # Set the range to be acceptable based on the daily calories goal
            daily_min_cal = self.calorie_target - 75
            daily_max_cal = self.calorie_target + 75

            # If within target, mark meal as completed
            if daily_min_cal < total_calories < daily_max_cal:
                meal_completed = True

            # Otherwise, start again
            else:
                self.todays_meals = []
                self.shuffle_recipes()
                attempts += 1

        if attempts >= 1000:
            raise FindRecipeError("Sorry, we were unable to find a suitable meal plan for you with the current calorie target and available recipes. Please consider one of the following options:\n1. Adjust your daily calorie target to a different target.\n2. Add more recipes to your collection.\n3. Try generating a meal plan for a different number of days.")


    # Function to print the days meal plan once it's been set
    def print_daily_meal(self):
        total_calories = 0
        semantic_meal_names = ["Breakfast","Lunch", "Dinner", "Snack 1", "Snack 2"] # Meal names readable and with meaning for the user

        # Zip dict and list together to iterate through both
        for meal_name, semantic_name in zip(self.todays_meals, semantic_meal_names):
            total_calories += int(meal_name['calories'])
            print(f"{semantic_name}: {meal_name['title']} ({
                  meal_name['calories']} calories) ")
            print(f"Ingredients: {meal_name['ingredients']}\n ")

        print(f"\nThe total calories for the day is: {total_calories}\n")


    # Check with user if they're happy with the meals for the day
    def day_check(self):
        while True:
            try:
                self.day_result = input("What do you think of these meals?\nEnter 's' to save them or 'n' to generate a new meal plan: ").lower()
                if self.day_result in ['s', 'n']:
                    break
                else:
                    print("Invalid input. Please enter either 's' or 'n'.")
            except InvalidInputError:
                print("Invalid input. Please enter either 's' or 'n'.")
    