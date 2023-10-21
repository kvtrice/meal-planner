# Import statements 
import pprint
import user_plan
import recipes
from meals import Day

#----------------------------------------------------------------

def generate_new_meal_plan(day):
    day.todays_meals = []  # Reset the current day's meals
    day.set_meals()  # Generate a new meal plan
    day.print_daily_meal()  # Print the new meal plan

def main():

    # Welcome
    print(f"Welcome to Meal Planner!\n")

    while True:
        # Entry point
        user_action = input("What would you like to do?\nEnter 'n' to start a new meal plan\nEnter 'a' to add a new recipe\nEnter 'v' to view all recipes\nOr enter 'q' to quit:\n").lower()

        if user_action == 'a':
            recipes.add_recipe()

        elif user_action == 'v':
            recipes.display_all_recipes()

        elif user_action == 'n':

            # Generate a User object
            user = user_plan.User()

            # Continuously loop until the user is happy with their meal plan
            while True:

                # Create a Day object and set the calorie range and daily calories
                day = Day(user.calorie_range, user.calorie_target)

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
                    change_calorie_target = input(f"Do you want to change your daily calorie target of {day.daily_calories} calories? Enter 'y' to change or 'n' to keep your curent target: ").lower()

                    # If yes, reset calories
                    if change_calorie_target == 'y':
                        user.set_calorie_target()

                    elif change_calorie_target == 'n':
                        continue

                    else:
                        raise Exception("Invalid input. Please enter either 'y' or 'n'.")
            
                else:
                    raise Exception("Invalid input. Please enter either 's' or 'n'.")
                
                print("Regenerating meal plan...")

        elif user_action == 'q':
            quit()
        else:
            raise Exception("Invalid input. Please enter 'n', 'a' 'v' or 'q'.")

if __name__ == "__main__":
    main()


