from admin import Admin
from user import RegularUser

admin = Admin("Admin", "admin")
user = RegularUser("Sh", "sh")

def show_admin_menu():
    print("\nAdmin Menu:")
    print("1. Add Recipe")
    print("2. Delete Recipe")
    print("3. View Recipes")
    print("4. Log Out")

def show_user_menu():
    print("\nUser Menu:")
    print("1. View Recipes")
    print("2. Search Recipe")
    print("3. Add to Favorites")
    print("4. View Favorites")
    print("5. Logout")

def login():
    while True:
        print("\t\t\tWELCOME TO CHEF'S CANVAS \U0001F469\U0000200D\U0001F373 \U0001F373")
        print("LOGIN")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if admin.login(username, password):
            print("Welcome Admin!")
            while True:
                show_admin_menu()
                choice = input("Enter your choice: ")
                if choice == '1':
                    admin.add_recipe()
                elif choice == '2':
                    admin.delete_recipe()
                elif choice == '3':
                    admin.view_recipes()
                elif choice == '4':
                    print("Logging out. Bye Bye!!")
                    break
                else:
                    print("Invalid choice \u274C. Try again!!")

        elif user.login(username, password):
            print(f"\nWelcome {username} \U0001F44B")
            while True:
                show_user_menu()
                choice = input("Enter what you want to do: ")
                if choice == '1':
                    user.view_recipes(admin.recipes)
                elif choice == '2':
                    search = input("Enter recipe name/cuisine/tags to search for: ")
                    results = user.search_recipe(admin.recipes, search)
                    if results:
                        for recipe in results:
                            print(f"Recipe Name: {recipe['name']}, Cuisine: {recipe['cuisine']}")
                    else:
                        print("No recipes found!!")
                elif choice == '3':
                    fav_name = input("Enter recipe name to add to favorites: ")
                    for recipe in admin.recipes:
                        if recipe['name'].lower() == fav_name.lower():
                            user.add_to_favorites(recipe)
                            break
                    else:
                        print(f"Recipe '{fav_name}' not found!")
                elif choice == '4':
                    user.view_favorites()
                elif choice == "5":
                    print("Logging out. Bye Bye!!")
                    break
                else:
                    print("Invalid choice \u274C. Try again!!")

        else:
            print("User not recognized \U0000274C. Try again.")

login()