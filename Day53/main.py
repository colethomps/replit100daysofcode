print("RPG Inventory")

inventory = []

try:
    with open("inventory.txt", "r") as f:
        inventory = eval(f.read())

except FileNotFoundError:
    print("Inventory file not found. Creating a new one.")

while True:
    print("\nOptions:")
    print("1: Add Item")
    print("2: Remove Item")
    print("3: View Item Count")
    print("4: Exit")

    option = input("Enter your choice: ")

    if option == "1":
        item = input("Input the item to add: ").capitalize()
        inventory.append(item)
        print(f"{item} added to inventory")
    elif option == "2":
        item = input("Input the item to remove: ").capitalize()
        if item in inventory:
            inventory.remove(item)
            print(f"{item} has been removed from inventory")
        else:
            print(f"{item} not found in inventory")
    elif option == "3":
        item = input("Input the item to view: ").capitalize()
        count = inventory.count(item)
        print(f"You have {count} {item}(s) in your inventory")
    elif option == "4":
        with open("inventory.txt", "w") as f:
            f.write(str(inventory))
        print("Exiting the RPG Inventory. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a valid option (1-4).")
