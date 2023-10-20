
# Define User class
class User():
    def __init__(self):
        self.daily_calories = 0
        self.calorie_range = 0
        # Call get_daily_calories function when initializing a new user
        self.get_daily_calories()

    def __repr__(self):
        return (f"Calorie Target: {self.daily_calories}. Calorie Range: {self.calorie_range}")

    # Function to get a users daily calorie goal / target
    def get_daily_calories(self):
        try:
            # Prompt for user input
            self.daily_calories = int(input("What is your daily calorie target? Please enter a target between 1400 - 3000 Calories: "))

            # Check to match the entered calorie target against the 5 specified ranges
            # Ranges are used later to determine how many calories should be in each specific meal
            if 1400 <= self.daily_calories <= 1700:
                self.calorie_range = 1
            elif 1701 <= self.daily_calories <= 2000:
                self.calorie_range = 2
            elif 2001 <= self.daily_calories <= 2300:
                self.calorie_range = 3
            elif 2301 <= self.daily_calories <= 2600:
                self.calorie_range = 4
            elif 2601 <= self.daily_calories <= 3000:
                self.calorie_range = 5
                
            # If not in one of these ranges then raise an exception
            elif self.daily_calories < 1400 or self.daily_calories > 3000: 
                raise UnboundLocalError("Calorie target must be a number between 1400 and 3000. Please enter a valid number.")

        # Raise exception if a string is entered rather than a number   
        except ValueError:
            print(("Calorie target cannot be a string! Please enter a valid calorie target between 1400 and 3000."))