import csv

# ----------------------------------------------------------------

def add_recipe():
    try:
        # Prompt user for recipe information
        new_title = input("What is the name of the recipe?: ")
        new_ingredients = input(
            "What are the ingredients of the recipe? (For 1 serving): ")
        new_calories = int(
            input("How many calories in this recipe? (For 1 serving): "))

        # Raise Exception of calorie number is less than 0
        if new_calories < 0:
            raise ValueError(
                "Calories can't be less than 0. Please enter a valid number.")

        # Turn the new recipe details into a dictionary
        new_recipe = {'title': new_title,
                      'ingredients': new_ingredients, 'calories': new_calories}

        # Append that dictionary to the existing CSV file (all recipes)
        with open(r'recipes.csv', 'a', newline='') as f:
            fieldnames = ['title', 'ingredients', 'calories']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(new_recipe)

        # Confirmationg for the user - recipe successfully added
        print(f"Your new recipe '{
              new_recipe['title']}' has successfully been added!")

    # Raise exception if a string is entered for the recipe calories
    except ValueError:
        print("Calories cannot be a string! Please enter a valid number.")


# Function to display all recipes to the user in a readable format (on-screen)
def display_all_recipes():
    with open('recipes.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['title']}: {row['ingredients']}. Calories: {row['calories']}\n")


# Function to open and read the CSV, get all recipes and store in a list -->
def get_recipes():
    with open('recipes.csv', 'r') as f:
        recipes_list = list(csv.DictReader(f))
        return recipes_list