# Import statements 
import pprint
import recipes
from meals import Day

#----------------------------------------------------------------

def generate_new_meal_plan(day):
    day.todays_meals = []  # Reset the current day's meals
    day.set_meals()  # Generate a new meal plan
    day.print_daily_meal()  # Print the new meal plan

def main():

    print(f"Hey, welcome to Meal Planner! Please choose from one of the actions below to get started\n") # Welcome

    while True:
        user_action = input("What would you like to do?\nEnter 'a' to add a new recipe\nEnter 'v' to view all recipes\nEnter 'n' to start a new meal plan for one day\nEnter 'c' to start a new meal plan for a custom number of days\nOr enter 'q' to quit:\n").lower() # Entry point

        if user_action == 'a':
            recipes.add_recipe()

        elif user_action == 'v':
            recipes.display_all_recipes()

        elif user_action == 'n':

            # Continuously loop until the user is happy with their meal plan
            while True:

                # Create a Day object and set the calorie range and daily calories
                day = Day()

                # Set the meals for the day
                day.set_meals()

                # Print the daily meal plan
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
                    change_calorie_target = input(f"Do you want to change your daily calorie target of {day.calorie_target} calories? Enter 'y' to change or 'n' to keep your curent target: ").lower()

                    # If yes, reset calories
                    if change_calorie_target != 'y' or change_calorie_target != 'n':
                        raise Exception("Invalid input. Please enter either 'y' or 'n'.")
            
                else:
                    raise Exception("Invalid input. Please enter either 's' or 'n'.")
                
                print("Regenerating meal plan...")

        # elif user_action == 'c':

        elif user_action == 'q':
            quit()
        else:
            raise Exception("Invalid input. Please enter 'n', 'a' 'v' or 'q'.")

if __name__ == "__main__":
    main()


