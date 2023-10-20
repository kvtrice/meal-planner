import csv

def add_recipe():
    try:
        new_title = input("What is the name of the recipe?: ")
        new_ingredients = input("What are the ingredients of the recipe? (For 1 serving): ")
        new_calories = int(input("How many calories in this recipe? (For 1 serving): "))
        
        if new_calories < 0:
            raise ValueError("Calories can't be less than 0. Please enter a valid number.")
        

        new_recipe = {'title': new_title, 'ingredients': new_ingredients, 'calories': new_calories}

        with open(r'recipes.csv', 'a', newline='') as f:
            fieldnames = ['title', 'ingredients', 'calories']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerow(new_recipe)

        print(f"Your new recipe '{new_recipe['title']}' has successfully been added!")

    except ValueError:
        print("Calories cannot be a string! Please enter a valid number.")

def get_all_recipes():
    with open('recipes.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['title']}: {row['ingredients']}. Calories: {row['calories']}\n")

