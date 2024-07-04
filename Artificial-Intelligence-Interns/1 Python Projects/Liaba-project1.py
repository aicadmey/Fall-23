print("Welcome to Laiba Restaurents")
food_inventory = {}

while True:
    print("\nFood Management System")
    print("1. Add a food item")
    print("2. Remove a food item")
    print("3. View food inventory")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        food_name = input("Enter the name of the food item: ")
        food_quantity = int(input("Enter the quantity: "))
        food_inventory[food_name] = food_inventory.get(food_name, 0) + food_quantity
        print(f"{food_quantity} {food_name}(s) added to the inventory.")

    elif choice == "2":
        food_name = input("Enter the name of the food item to remove: ")
        if food_name in food_inventory:
            food_quantity = int(input("Enter the quantity to remove: "))
            if food_quantity >= food_inventory[food_name]:
                del food_inventory[food_name]
            else:
                food_inventory[food_name] -= food_quantity
            print(f"{food_quantity} {food_name}(s) removed from the inventory.")
        else:
            print(f"{food_name} not found in the inventory.")

    elif choice == "3":
        print("\nFood Inventory:")
        for food, quantity in food_inventory.items():
            print(f"{food}: {quantity}")
    
    elif choice == "4":
        print("Exiting the Food Management System.")
        break

    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")
