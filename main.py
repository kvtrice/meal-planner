# Import statements 
import recipes
import argparse
from meals import Day, InvalidInputError

# ----------------------------------------------------------------

CALORIE_MIN = 1400
CALORIE_MAX = 3000
DAYS_MIN = 1
DAYS_MAX = 14

# Get user calorie target
def get_calorie_target(user_input):
    calorie_target = int(user_input)
    if CALORIE_MIN <= calorie_target <= CALORIE_MAX:
        return calorie_target  
    else:
        raise InvalidInputError("Calorie target must be a number between 1400 and 3000. Please enter a valid number.")

# Get number of days the suer wants meal plans for
def get_num_days(user_input):
    num_days = int(user_input)
    if DAYS_MIN <= num_days <= DAYS_MAX:
        return num_days
    else:
        raise InvalidInputError("Number of days must be a number between 1 and 14. Please enter a valid number.")

def get_user_action():
    return input("What would you like to do?\na = Add a new recipe\nv = View all recipes\nn = Start a new meal plan\nq = quit\n").lower()

def main():

    # Argparse to add recipe direct from the commandline
    parser = argparse.ArgumentParser(description="Meal Planner: Meal planning made simple")

    parser.add_argument("--title", help="Name of the recipe")
    parser.add_argument("--ingredients", help="Ingredients for 1 serving")
    parser.add_argument("--calories", type=int, help="Calories for 1 serving")

    args = parser.parse_args()

    # Check if a recipe has been added from the command line
    if args.title or args.ingredients or args.calories:
        recipes.add_recipe_from_cli(args) # Call the add recipe via cli function and pass the args

    # Welcome
    print(f"\nHey, welcome to Meal Planner! Please choose from one of the actions below to get started\n")

    while True:
        try:
            user_action = get_user_action()

            if user_action == 'a': 
                recipes.add_recipe() # Add a new recipe
            
            elif user_action == 'v': 
                recipes.display_all_recipes() # View all recipes
            
            elif user_action == 'n': # Start new meal plan
                num_days_input = input("How many days would you like to get a meal plan for?: ")
                num_days = get_num_days(num_days_input) # Get num days user wants meal plans for
                calorie_target_input = input(f"What is your daily calorie target? Please enter a target between {CALORIE_MIN} - {CALORIE_MAX} Calories: ")
                calorie_target = get_calorie_target(calorie_target_input)  # Get calorie target for all days

                # Continuously loop until the user is happy with their meal plan
                while True:
                    all_meals = [] # Empty list to add meals to
                    
                    for i in range(num_days):
                        day = Day(calorie_target) # Create a Day object and set the calorie range and daily calories
                        day.set_meals() # Set the meals for the day
                        all_meals.append(day) # Append set meals to all_meals list
                    
                    # Print the meal plan for all days
                    print("\nHere are your daily meal plans:\n")
                    day_number = 1
                    for day in all_meals:
                        print(f"Day {day_number} Meal Plan:\n")
                        day.print_daily_meal() # Call print function for each daily meal
                        day_number += 1 # Increment number

                    # Check if user is happy with their meals
                    day.result = input("What do you think of these meals?\nEnter 's' to save them or 'n' to generate a new meal plan: ").lower()

                    if day.result == 's':
                        if day.save_meal_plan(all_meals): # Save the meals to a file
                            break

                    elif day.result == 'n':
                        if day.check_calorie_change(): # Check if user wants to change calorie target is True
                            calorie_target_input = input(f"Regenerating meal plan...\nWhat is your daily calorie target? Please enter a target between {CALORIE_MIN} - {CALORIE_MAX} Calories: ")
                            calorie_target = get_calorie_target(calorie_target_input)

                    else:
                        raise InvalidInputError("Invalid input. Please enter 's' to save or 'n' to generate a new meal plan")
    
            elif user_action == 'q':
                print("See you again soon!")
                quit() # Quit the program

            else:
                raise InvalidInputError("Invalid input. Please enter one of: 'a' 'v', 'n' or 'q'.")

        # Raise exception if anything outside of 'a', 'v', 'v', 'c' or 'q' is entered
        except InvalidInputError as e:
            print(e)
        

if __name__ == "__main__":
    main()
