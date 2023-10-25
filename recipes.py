import csv

# ----------------------------------------------------------------

# Function to add recipe to CSV file
def add_recipe_to_CSV(new_recipe):
    # Append dictionary to the existing CSV file (all recipes)
    with open(r'recipes.csv', 'a', newline='') as f:
        fieldnames = ['title', 'ingredients', 'calories']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow(new_recipe)

    # Confirmation for the user - recipe successfully added
    print(f"Your new recipe '{new_recipe['title']}' has successfully been added!")


# Function to add a recipe from commandline
def add_recipe_from_cli(args):
    # Process the provided command-line arguments and add the recipe
    new_recipe = {'title': args.title, 'ingredients': args.ingredients, 'calories': args.calories}

    # Add recipe to CSV file
    add_recipe_to_CSV(new_recipe)

# Function to add recipe within the app
def add_recipe():
    new_title = input("What is the name of the recipe?: ")
    new_ingredients = input(
        "What are the ingredients of the recipe? (For 1 serving): ")
    while True:
        try: 
            new_calories = int(
            input("How many calories in this recipe? (For 1 serving): "))
            # Raise Exception if calorie number is less than 0
            if new_calories < 0:
                raise ValueError(
                    "Calories cannot be less than 0. Please enter a valid number.")
            break
        except ValueError:
            print("Invalid Input. Please enter an integer above 0.")

    # Turn the new recipe details into a dictionary
    new_recipe = {'title': new_title,'ingredients': new_ingredients, 'calories': new_calories}
    # Add recipe to CSV file
    add_recipe_to_CSV(new_recipe)

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