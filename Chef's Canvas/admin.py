import time

class Admin:
    def _init_(self, username, password):
        self.username = username
        self.password = password
        self.recipes = [
        {
            "name": "Spaghetti Carbonara",
            "cuisine": "Italian",
            "ingredients": ["spaghetti", "eggs", "parmesan cheese", "bacon", "black pepper"],
            "tags": ["pasta", "classic"],
            "instructions": [
                "Boil the spaghetti until al dente.",
                "Cook the bacon until crispy.",
                "Mix eggs and parmesan cheese in a bowl.",
                "Combine spaghetti, bacon, and egg mixture over low heat.",
                "Season with black pepper and serve."
            ]
        },
        {
            "name": "Chicken Curry",
            "cuisine": "Indian",
            "ingredients": ["chicken", "onion", "tomatoes", "garlic", "ginger", "spices", "coconut milk"],
            "tags": ["spicy", "curry"],
            "instructions": [
                "Saute onions, garlic, and ginger until golden.",
                "Add spices and cook for a minute.",
                "Add chicken and cook until browned.",
                "Add tomatoes and simmer until tender.",
                "Stir in coconut milk and simmer until cooked through."
            ]
        },
        {
            "name": "Tacos",
            "cuisine": "Mexican",
            "ingredients": ["tortillas", "ground beef", "lettuce", "tomatoes", "cheese", "salsa"],
            "tags": ["snack", "quick"],
            "instructions": [
                "Cook ground beef with seasoning.",
                "Warm the tortillas.",
                "Assemble tacos with beef, lettuce, tomatoes, cheese, and salsa.",
                "Serve immediately."
            ]
        },
        {
            "name": "Caesar Salad",
            "cuisine": "Italian",
            "ingredients": ["romaine lettuce", "croutons", "parmesan cheese", "Caesar dressing"],
            "tags": ["healthy", "salad"],
            "instructions": [
                "Chop the romaine lettuce.",
                "Add croutons and parmesan cheese.",
                "Drizzle Caesar dressing and toss well.",
                "Serve chilled."
            ]
        },
        {
            "name": "Pancakes",
            "cuisine": "American",
            "ingredients": ["flour", "milk", "eggs", "butter", "syrup"],
            "tags": ["breakfast", "sweet"],
            "instructions": [
                "Mix flour, milk, and eggs into a batter.",
                "Heat butter in a pan and pour batter to form pancakes.",
                "Cook until golden brown on both sides.",
                "Serve with syrup."
            ]
        },
        {
            "name": "Sushi Rolls",
            "cuisine": "Japanese",
            "ingredients": ["sushi rice", "nori sheets", "fish", "vegetables", "soy sauce"],
            "tags": ["seafood", "traditional"],
            "instructions": [
                "Cook sushi rice and let it cool.",
                "Place rice on nori sheets and add fish and vegetables.",
                "Roll tightly and slice into pieces.",
                "Serve with soy sauce."
            ]
        },
        {
            "name": "Veggie Stir Fry",
            "cuisine": "Chinese",
            "ingredients": ["vegetables", "soy sauce", "garlic", "ginger", "oil"],
            "tags": ["vegan", "quick"],
            "instructions": [
                "Heat oil in a pan.",
                "Add garlic and ginger, then vegetables.",
                "Stir fry with soy sauce until cooked.",
                "Serve hot."
            ]
        },
        {
            "name": "Beef Stroganoff",
            "cuisine": "Russian",
            "ingredients": ["beef", "onion", "mushrooms", "sour cream", "pasta"],
            "tags": ["hearty", "comfort"],
            "instructions": [
                "Cook beef until browned.",
                "Add onions and mushrooms, then cook until tender.",
                "Stir in sour cream and simmer.",
                "Serve over pasta."
            ]
        },
        {
            "name": "Falafel Wraps",
            "cuisine": "Middle Eastern",
            "ingredients": ["falafel", "pita bread", "hummus", "lettuce", "tomatoes"],
            "tags": ["vegan", "wrap"],
            "instructions": [
                "Cook falafel until crispy.",
                "Spread hummus on pita bread.",
                "Add falafel, lettuce, and tomatoes.",
                "Wrap and serve."
            ]
        },
        {
            "name": "Chocolate Cake",
            "cuisine": "Dessert",
            "ingredients": ["flour", "cocoa powder", "sugar", "eggs", "butter", "chocolate"],
            "tags": ["dessert", "baking"],
            "instructions": [
                "Mix flour, cocoa powder, and sugar.",
                "Add eggs and melted butter to form a batter.",
                "Pour into a baking pan and bake at 350°F for 30 minutes.",
                "Melt chocolate for frosting and spread over the cooled cake.",
                "Serve and enjoy!"
            ]
        }
    ]

    def login(self, username, password):
        return self.username == username and self.password == password

    def add_recipe(self):
        print("\nAdd a new recipe:")
        name = input("Enter recipe name: ")
        cuisine = input("Enter cuisine: ")
        ingredients = input("Enter ingredients (comma-separated): ").split(",")
        tags = input("Enter tags (comma-separated): ").split(",")

        print("\nEnter step-by-step instructions (type 'done' when finished):")
        instructions = []
        step_number = 1
        while True:
            step = input(f"Step {step_number}: ")
            if step.lower() == "done":
                break
            instructions.append(step)
            step_number += 1

        current_time = time.strftime("%Y-%m-%d %H:%M:%S")

        recipe = {
            'name': name,
            'cuisine': cuisine,
            'ingredients': [ingredient.strip() for ingredient in ingredients],
            'tags': [tag.strip() for tag in tags],
            'instructions': instructions,
            'date_added': current_time
        }

        self.recipes.append(recipe)
        print(f"\nRecipe '{name}' added successfully at {current_time}! \U0001F973")

    def delete_recipe(self):
        if not self.recipes:
            print("No recipes to delete.")
            return
        name = input("Enter the recipe name to delete: ")
        for recipe in self.recipes:
            if recipe["name"].lower() == name.lower():
                self.recipes.remove(recipe)
                print(f"Recipe '{name}' deleted successfully.")
                return
        print(f"Recipe '{name}' not found.")

    def view_recipes(self):
        if not self.recipes:
            print("No recipes available.")
        else:
            print("\nAvailable Recipes:")
            for index, recipe in enumerate(self.recipes, 1):
                print(f"{index}. Name: {recipe['name']}, Cuisine: {recipe['cuisine']}")