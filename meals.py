import random
from recipes import get_recipes

# ----------------------------------------------------------------

class Day():
    def __init__(self):
        self.calorie_target = 0
        self.get_calorie_target() # Get calorie target upon initialisation
        self.meal_calories = {}  # Store meal calories based on the users calorie target
        # Set the meal calories (based on the calorie range) each time a day is initialized
        self.set_meal_calories(self.calorie_target)
        self.todays_meals = []  # Empty list for todays meals
        self.day_result = None

    def get_calorie_target(self):
        try:
            self.calorie_target = int(input("What is your daily calorie target? Please enter a target between 1400 - 3000 Calories: ")) # Prompt for user input

            # If not in one of these ranges then raise an exception
            if self.calorie_target < 1400 or self.calorie_target > 3000:
                raise UnboundLocalError(
                    "Calorie target must be a number between 1400 and 3000. Please enter a valid number.")

        # Raise exception if a string is entered rather than a number
        except ValueError:
            print(("Calorie target cannot be a string! Please enter a valid calorie target between 1400 and 3000."))

    # Set the calories required for each meal based on user calorie target
    def set_meal_calories(self, calorie_target):
        # Based on each calorie_range, set the dictionary to equal the below specified calories
        if 1400 <= self.calorie_target <= 1700:
            self.meal_calories = {
                "M1": 400,
                "M2": 400,
                "M3": 500,
                "M4": 250,
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
        while meal_completed == False and attempts < 100:
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
                        raise Exception(
                            "Sorry, we couldn't find a recipe for this meal.")

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

        if attempts >= 100:
            raise Exception(
                "Sorry, we were unable to find a suitable meal plan for you at this time. Please try again with a different calorie target or add some more recipes.")

    # Function to print the days meal plan once it's been set
    def print_daily_meal(self):
        total_calories = 0
        print(f"\nBased on your daily calorie goal, here is today's meals: \n")
        # Meal names readable and with meaning for the user
        semantic_meal_names = ["Breakfast",
                               "Lunch", "Dinner", "Snack 1", "Snack 2"]

        # Zip dict and list together to iterate through both
        for meal_name, semantic_name in zip(self.todays_meals, semantic_meal_names):
            total_calories += int(meal_name['calories'])
            print(f"{semantic_name}: {meal_name['title']} ({
                  meal_name['calories']} calories) ")
            print(f"Ingredients: {meal_name['ingredients']}\n ")

        print(f"\nThe total calories for the day is: {total_calories}\n")

    # Check with user if they're happy with the meals for the day
    def day_check(self):
        self.day_result = input(
            "What do you think of these meals?\nEnter 's' to save them or 'n' to generate a new meal plan: ").lower()
