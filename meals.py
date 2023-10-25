import random
import datetime
import time
from recipes import get_recipes

# ----------------------------------------------------------------
# Exception for invalid inputs
class InvalidInputError(Exception):
    pass

# Exception for when unable to find a valid recipe
class FindRecipeError(Exception):
    pass

class Day():
    def __init__(self, calorie_target):
        self.calorie_target = calorie_target
        self.meal_calories = {}  # Store meal calories based on the users calorie target
        # Set the meal calories (based on the calorie range) each time a day is initialized
        self.set_meal_calories()
        self.todays_meals = []  # Empty list for todays meals
        self.semantic_names = ["Breakfast","Lunch", "Dinner", "Snack 1", "Snack 2"]
        self.result = None

    # Set the calories required for each meal based on user calorie target
    def set_meal_calories(self):
        # Based on each calorie_range, set the dictionary to equal the below specified calories
        if 1400 <= self.calorie_target <= 1700:
            self.meal_calories = {
                "M1": 300,
                "M2": 350,
                "M3": 500,
                "M4": 200,
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
                   no_meal_err = {}
                   no_meal_err = {"title":"Oops! No meal found. This can happen if there aren't enough recipes calorie range for your target. Try adding some more recipes!", "ingredients": "None", "calories": 0}
                   self.todays_meals.append(no_meal_err)
                        

            # Check that meal total is acceptable close to the users target calories
            total_calories = 0
            # Sum each meals calories together to find the total
            for meal in self.todays_meals:
                total_calories += int(meal['calories'])

            # Set the range to be acceptable based on the daily calories goal
            daily_min_cal = self.calorie_target - 100
            daily_max_cal = self.calorie_target + 100

            # If within target, mark meal as completed
            if daily_min_cal < total_calories < daily_max_cal:
                meal_completed = True

            # Otherwise, start again
            else:
                self.todays_meals = []
                self.shuffle_recipes()
                attempts += 1


    # Function to print the days meal plan once it's been set
    def print_daily_meal(self):
        total_calories = 0

        # Zip dict and list together to iterate through both
        for meal_name, semantic_name in zip(self.todays_meals, self.semantic_names):
            total_calories += int(meal_name['calories'])
            print(f"{semantic_name}: {meal_name['title']} ({meal_name['calories']} calories) ")
            print(f"Ingredients: {meal_name['ingredients']}\n ")

        print(f"\nThe total calories for the day is: {total_calories}\n")

    # Print user meals to a text file
    def output_meals(self, all_meals, filename):
        f = open(filename, 'w')
        day_number = 1

        # Get current time
        t = time.localtime()
        current_time = time.strftime("%H:%M", t)

        # Get current date
        d = datetime.datetime.today()
        todays_date = d.strftime("%d-%m-%Y")

        f.write(f"\nRetrieved on {todays_date} at {current_time}.\n")

        for day in all_meals:
            f.write(f"\nDay {day_number} Meal Plan:\n")
            total_calories = 0
            
            # Write each meal to the file:
            for meal_name in day.todays_meals:

                # Attach semantic names to each meal
                semantic_name = self.semantic_names[day.todays_meals.index(meal_name)]
                
                # Nicely formatted meals for the text file
                meal_str = f"{semantic_name}: {meal_name['title']} ({meal_name['calories']} calories)\nIngredients: {meal_name['ingredients']}\n"
                
                # Write to the text file
                f.write(meal_str)
                
                # Increase the calories each meal to sum them
                total_calories += int(meal_name['calories'])

            # Print the calories per day
            f.write(f"The total calories for the day is: {total_calories}\n")
            day_number += 1 # Increment day
      
    # Check with user if they're happy with the meal plan
    def save_meal_plan(self, all_meals):
        filename = input("Great, let's save these for you. What should the save file be called?: ") # Get filename from user
        filename = filename + '.txt'
        self.output_meals(all_meals, filename) # Save to file via output_meal function
        print("\nYour meals have been saved!\n")
        return True

    # Check with user if they want to change their calorie target when re-rolling their meal plan
    def check_calorie_change(self, user_input):
        change_calories = user_input.lower()
        if change_calories == 'y':
            return True
        else:
            return False
            
    