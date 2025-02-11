def collect_recipe_data():
    # Initialize a list to store recipes
    recipes = []

    while True:
        # Collect basic recipe details
        print("\nEnter the recipe details:")
        name = input("Recipe Name: ")
        cuisine = input("Cuisine: ")
        ingredients = input("Ingredients (comma-separated): ").split(',')
        ingredients = [ingredient.strip() for ingredient in ingredients]  # Trim spaces

        # Collect step-by-step instructions
        instructions = []
        print("\nEnter step-by-step instructions. Type 'done' when finished:")
        step_number = 1
        while True:
            step = input(f"Step {step_number}: ")
            if step.lower() == "done":
                break
            instructions.append(step)
            step_number += 1

        # Store the recipe in the list
        recipes.append({
            "name": name,
            "cuisine": cuisine,
            "ingredients": ingredients,
            "instructions": instructions
        })

        # Ask if the user wants to add another recipe
        another = input("\nDo you want to add another recipe? (yes/no): ").lower()
        if another != "yes":
            break

    return recipes

# Run the function and print the stored recipes
if __name__ == "__main__":
    all_recipes = collect_recipe_data()
    print("\nStored Recipes:")
    for recipe in all_recipes:
        print("\nRecipe Name:", recipe["name"])
        print("Cuisine:", recipe["cuisine"])
        print("Ingredients:", ', '.join(recipe["ingredients"]))
        print("Instructions:")
        for i, step in enumerate(recipe["instructions"], 1):
            print(f"  Step {i}: {step}")
