# Import statements 
import recipes
import argparse
from meals import Day, InvalidInputError

# ----------------------------------------------------------------

# Get user calorie target
def get_calorie_target():
    while True:
        try:
            calorie_target = int(input("What is your daily calorie target? Please enter a target between 1400 - 3000 Calories: ")) # Prompt for user input
            
            if 1400 <=  calorie_target <= 3000:
                return calorie_target  
            else:
                print("Calorie target must be a number between 1400 and 3000. Please enter a valid number.")

        # Raise exception if a string is entered rather than a number
        except ValueError:
            print("Calorie target must be a number between 1400 and 3000. Please enter a valid number.")

# Get number of days the suer wants meal plans for
def get_num_days():
    while True:
        try:
            num_days = int(input("How many days would you like to get a meal plan for?: "))

            if 0 < num_days <= 14:
                return num_days
            else:
                print("Number of days must be a number between 1 and 14. Please enter a valid number.")

        # Raise exception if a string is entered rather than a number
        except ValueError:
            print("Number of days must be a number between 1 and 14. Please enter a valid number.")

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

    # ----------------------------------------------------------------
    # Main application start

    # Welcome
    print(f"\nHey, welcome to Meal Planner! Please choose from one of the actions below to get started\n")

    while True:
        try:
            user_action = input("What would you like to do?\na = Add a new recipe\nv = View all recipes\nn = Start a new meal plan\nq = quit\n").lower() # Entry point

            # Add a new recipe ----------------------------------------------------------------
            if user_action == 'a':
                recipes.add_recipe()

            
            # View all recipes ----------------------------------------------------------------
            elif user_action == 'v':
                recipes.display_all_recipes()

            
            # Create a new Meal plan for custom number of days --------------------------------
            elif user_action == 'n':
                num_days = get_num_days() # Get num days user wants meal plans for
                calorie_target = get_calorie_target()  # Get calorie target for all days

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
                    
                    while True:

                        # Check if user is happy with their meals
                        day.result = input("What do you think of these meals?\nEnter 's' to save them or 'n' to generate a new meal plan: ").lower()

                        if day.result == 's':
                            day.save_meal_plan(all_meals) # Save the meals to a file
                            break

                        elif day.result == 'n':
                            if day.check_calorie_change(): # Check if user wants to change calorie target is True
                                calorie_target = get_calorie_target()
                                print("\nRegenerating meal plan...\n")
                                break

                        else:
                            raise InvalidInputError("Invalid input. Please enter 's' to save or 'n' to generate a new meal plan")
                

            # Quit the program -------------------------------------------------------------
            elif user_action == 'q':
                print("See you again soon!")
                quit()

            else:
                raise InvalidInputError("Invalid input. Please enter one of: 'a' 'v', 'n' or 'q'.")

        # Raise exception if anything outside of 'a', 'v', 'v', 'c' or 'q' is entered
        except InvalidInputError as e:
            print(e)
        

if __name__ == "__main__":
    main()
