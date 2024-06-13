"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                                LAB 3
-----------------------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Develop a user interface for the Inventory Management System. This interface will
               allow users to interact with the InventoryManager to add, update, remove, and view
               items in the inventory using a command-line interface.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Step 1: Import necessary classes (Item class from lab1, InventoryManager class from lab2)
from lab1 import Item 
from lab2 import ItemManager

# Step 2: Define an add_item function that prompts the user for item details and adds the item to the inventory
def add_item_ui(inventory):
    name = input("Please enter the name of the item: ")
    price = input("Please enter the price of the item: ")
    quantity = input("Please enter the quantity: ")
    item = Item(name, price, quantity)
    inventory.add_item(item)
    
    
def update_item_ui(inventory):
    name = input("Enter item name to update: ")
    price = input("Enter new price: ")
    if price:
        price = float(price)
    else:
        price = None
    if quantity:
        quantity = int(quantity)
    if manager.update_item_quantity(name, quantity):
        print("Item update successfully")
    else:
        print("Failed to update yo price")
        
def remove_item_ui(inventory):
    name = input("What item would you like to remove: ")
    inventory.remove_item(name)
    
def display_item_ui(inventory):
    

# Step 3: Define an update_item function that prompts the user for item details and updates the item in the inventory


# Step 4: Define a remove_item function that prompts the user for an item name and removes the item from the inventory


# Step 5: Define a display_inventory function that displays all items in the inventory


def main():
    # Step 6: Initialise an instance of InventoryManager
    inventory = ItemManager()
    

    # Step 7: Use the actions dictionary to map user input to the corresponding functions
    actions = {
        '1': add_item_ui,
        '2': update_item_ui,
        '3': remove_item_ui,
        '4': display_item_ui,    }
    
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. Remove Item")
        print("4. Display Inventory")
        print("5. Exit")

        choice = input("Enter choice: ")

        # Step 8: Implement the logic to call the appropriate function based on user input
        
        
        # Exit the loop if the user chooses 5, otherwise display an error message for invalid choices

        if choice == '5':
            print("Exiting Program")
        elif choice in actions:
            actions[choice](inventory)
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()