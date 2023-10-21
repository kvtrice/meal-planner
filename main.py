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
day.print_daily_meal()
# pprint.pprint(day.todays_meals)



        # for row in reader:
        #     print(f"{row['title']}: {row['ingredients']}. Calories: {row['calories']}\n")


# Check with the usre if they're happy with it
# If no, they can re-roll it
# If yes, print to a file

# ----------------------------------------------------------------




