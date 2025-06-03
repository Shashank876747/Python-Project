def mainMenu():
    while True:
        # Display the main menue
        print()
        print('''### SHOPPING LIST ###
    
    Select a number for the action you want to do:
    
    1. View shopping list
    2. Add item to shopping list
    3. Remove item from shopping list
    4. Check if item is in shopping list
    5. Houw many items on shopping list
    6. Clear shopping list
    ''')

        # Ask the user to make a selection
        selection = input("Make your selection: ")

        # Determine wich action to take based on the user's selection
        if selection == "1":
            displayList()
        elif selection == "2":
            additem()
        elif selection == "3":
            removeitem()
        elif selection == "4":
            checkItem()
        elif selection == "5":
            listLength()
        elif selection == "6":
            clearlist()
        else:
            print("You did not make a valid selection")


# Add a few items to the shopping list
shopping_list = ["bread", "milk", "eggs", "cheese",]

# Display the items on the shopping list


def displayList():
    print()
    print("---SHOPPING LIST---")
    for i in shopping_list:
        print("*" + i)

# Add an item to the shopping list


def additem():
    item = input("Enter item you want to add to the shopping list: ")
    shopping_list.append(item)
    print(item + " has been added to the shopping list ")

# Remove an item from the shopping list


def removeitem():
    item = input("Witch item you like to remove from the shopping list: ")
    shopping_list.remove(item)
    print(item + " has been removed from the shopping list")


def checkItem():
    item = input("What item would you like to check on the shopping list: ")
    if item in shopping_list:
        print("Yes, " + item + " is on the shopping list")
    else:
        print("No, " + item + " is not on the shopping list")


def listLength():
    print("There are", len(shopping_list), " items on the shopping list")


def clearlist():
    shopping_list.clear()
    print("The shopping list is now empty.")


mainMenu()
