
# Define User class
class User():
    def __init__(self):
        self.calorie_target = 0
        self.calorie_range = 0
        self.set_calorie_target() # Call get_daily_calories function when initializing a new user

    def __repr__(self):
        return (f"Calorie Target: {self.calorie_target}. Calorie Range: {self.calorie_range}")

    # Function to get a users daily calorie goal / target
    def set_calorie_target(self):
        try:
            self.calorie_target = int(input(
                "What is your daily calorie target? Please enter a target between 1400 - 3000 Calories: ")) # Prompt for user input

            # Check to match the entered calorie target against the 5 specified ranges
            if 1400 <= self.calorie_target <= 1700:
                self.calorie_range = 1
            elif 1701 <= self.calorie_target <= 2000:
                self.calorie_range = 2
            elif 2001 <= self.calorie_target <= 2300:
                self.calorie_range = 3
            elif 2301 <= self.calorie_target <= 2600:
                self.calorie_range = 4
            elif 2601 <= self.calorie_target <= 3000:
                self.calorie_range = 5

            # If not in one of these ranges then raise an exception
            elif self.calorie_target < 1400 or self.calorie_target > 3000:
                raise UnboundLocalError(
                    "Calorie target must be a number between 1400 and 3000. Please enter a valid number.")

        # Raise exception if a string is entered rather than a number
        except ValueError:
            print(("Calorie target cannot be a string! Please enter a valid calorie target between 1400 and 3000."))
