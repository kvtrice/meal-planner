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
            except InvalidInputError:
                print("Calorie target must be a number between 1400 and 3000. Please enter a valid number.")


def main():

    # Argparse to add recipe from the commandline
    parser = argparse.ArgumentParser(description="Your app description")
    parser.add_argument("--title", required=True, help="Name of the recipe")
    parser.add_argument("--ingredients", required=True, help="Ingredients for 1 serving")
    parser.add_argument("--calories", type=int, required=True, help="Calories for 1 serving")

    args = parser.parse_args()

    # Check if a recipe as been added from the command line
    if args.title or args.ingredients or args.calories:
        # Call the add recipe via cli function and pass the args
        recipes.add_recipe_from_cli(args)

    # ----------------------------------------------------------------
    # Main application start

    # // Welcome
    print(f"Hey, welcome to Meal Planner! Please choose from one of the actions below to get started\n")

    while True:
        try:
            user_action = input("What would you like to do?\na = Add a new recipe\nv = View all recipes\nn = Start a new meal plan for one day\nc = Start a new meal plan for a custom number of days\nq = quit\n").lower() # Entry point

            # Add a new recipe ----------------------------------------------------------------
            if user_action == 'a':
                recipes.add_recipe()

            # View all recipes ----------------------------------------------------------------
            elif user_action == 'v':
                recipes.display_all_recipes()

            # Meal plan for one day -----------------------------------------------------------
            elif user_action == 'n':
                # Continuously loop until the user is happy with their meal plan
                while True:
                    # Get daily calorie target
                    calorie_target = get_calorie_target()
                    
                    # Create a Day object and parse in calorie_target
                    day = Day(calorie_target)

                    # Set the meals for the day
                    day.set_meals()

                    # Print the daily meal plan
                    print("\nBased on your daily calorie target, here are today's meals:\n")
                    day.print_daily_meal()

                    # Check with the user if they're happy with the meals for the day
                    day.day_check()  # Call the day_check method of the Day object

                    # Get the result from day_check
                    day_result = day.day_result

                    # Act based on the result
                    if day_result == 's':
                        print("Meals are saved!")
                        break
                    # If no
                    elif day_result == 'n':
                        # Also ask if want to change calorie target
                        change_calorie_target = input(f"Do you want to change your daily calorie target of {day.calorie_target} calories? Enter 'y' to change or 'n' to keep your current target: ").lower()

                        # Raise Exception if invalid input
                        if change_calorie_target != 'y' and change_calorie_target != 'n':
                            raise Exception("Invalid input. Please enter either 'y' or 'n'.")
                
                    # Raise Exception if invalid input
                    else:
                        raise Exception("Invalid input. Please enter either 's' or 'n'.")
                    
                    print("Regenerating meal plan...")

            # Meal plan for custom number of days -------------------------------------------
            elif user_action == 'c':
                # Continuously loop until the user is happy with their meal plan
                while True:
                    num_days = int(input("How many days would you like to get a meal plan for?: "))
                    custom_num_days = []

                    # Get calorie target for all days
                    custom_day_calorie_target = get_calorie_target()

                    for i in range(num_days):

                        # Create a Day object and set the calorie range and daily calories
                        custom_day = Day(custom_day_calorie_target)

                        # Set the meals for the day
                        custom_day.set_meals()

                        # Append set meals to a list
                        custom_num_days.append(custom_day)
                    
                    # Print the meal plan for all days
                    print("\nHere are your daily meal plans:\n")
                    day_number = 1
                    for day in custom_num_days:
                        print(f"Day {day_number} Meal Plan:\n")
                        day.print_daily_meal()
                        day_number += 1

                    # Check with the user if they're happy with the meals for the day
                    multi_day_result = input("What do you think of these meals?\nEnter 's' to save them or 'n' to generate a new meal plan: ").lower()

                    if multi_day_result == 's':
                        print("Meals are saved!")
                        break

            # Quit the program ---------------------------------------------------------------
            elif user_action == 'q':
                quit()

            else:
                raise InvalidInputError("Invalid input. Please enter one of: 'a' 'v', 'n', 'c' or 'q'.")

        # Raise exception if anything outside of 'a', 'v', 'v', 'c' or 'q' is entered
        except InvalidInputError as e:
            print(e)
        

if __name__ == "__main__":
    main()


