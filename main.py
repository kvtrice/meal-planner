import pprint
import user_plan
import recipes
from meals import Day

# User menu at start
# Welcome
# Add a recipe
# View all Recipes
# Start a new meal plan

# Add a recipe
# Call new_recipe()

# View all recipes
# Call view_all_recipes()

# ----------------------------------------------------------------

# Start a new Meal Plan

# Ask user for calories
# User enters cals
# Determine what range that calorie goal is in
user = user_plan.User()

# Based on the calorie goal, determine what calories can be in each type of meal
# create a day object, pass it the calorie goal + range from the User
day = Day(user.calorie_range, user.daily_calories)
day.set_meals()
print(day)
pprint.pprint(day.todays_meals)

# Once we have a calorie range for each meal type, we need to find a random meal for each


# Breakfast = 1 meal
# Lunch = 1 meal
# Dinner = 1 meal
# Snacks = 2 

# Once each meal is grabbed, append it to a list on the Day Class - this is their daily meal plan
# Add that day to a list on the User - this will become their weekly meal plan

# Once all meals are grabbed, sum the total calories for the day, based on the meals in the list
# Check that sum against what the user entered as their target.
# Is the sum within 100 cals either side? If yes - print
# If not, try again

# Once successful meal plan is arrived it, print it to the user

# Check with the usre if they're happy with it
# If no, they can re-roll it
# If yes, print to a file

# ----------------------------------------------------------------




