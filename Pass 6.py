# UNC AI Bootcamp Week 2 Homework 

# Challenge Instructions

# Create a food truck ordering system that allows a user to order food from a food truck. The system should allow the user to order multiple items and then print out a receipt with the total cost of the order.

#The system should allow the user to order multiple items and then print out a receipt with the total cost of the order.

#Menu
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}


# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = [] # This is a list of dictionaries

# Create an empty list. This list will later store a customer's order in dictionary format, as follows:
[
  {
    "Item name": "string", # This will be the menu item name from the menu dictionary
    "Price": float,
    "Quantity": int
  },
  {
    "Item name": "string", # This will be the menu item name from the menu dictionary
    "Price": float,
    "Quantity": int
  },
]

# 2. Ask the customer for their name and store it in a variable
def welcome_customer():
    # Ask the customer for their name and store it in a variable
    customer_name = input("What is your name? ") # Ask the customer for their name and store it in a variable
    return customer_name # Return the customer's name


# 3. Launch the store and present a greeting to the customer
print() # Print a blank line
print("John's Food Truck Ordering System - Copyright 2023. Press enter to get started.") # Launch the store and present a greeting to the customer
print("-" * 81) # Print a line to separate the greeting from the rest of the program

input() # Wait for the customer to press a key

# 4. Welcome the customer to the store by name
customer_name = welcome_customer()
print(f"Welcome to John's Food Truck, {customer_name}!") # Welcome the customer to the store by name
print("-" * 81) # Print a line to separate the greeting from the rest of the program
print() # Print a blank line

# 5. Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? (Choose 5 to exit.)") 
    print() # Print a blank line
    
    # Create a variable for the menu item number
    i = 1 # This will be used to number the menu items

    # Create a dictionary to store the menu for later retrieval
    menu_items = {} # This will be used to store the menu items

    # Print the options to choose from menu headings (all the first level dictionary items in menu).
    for key in menu.keys(): # Loop through the menu dictionary
        print(f"{i}: {key}") # Print the menu item number and menu item name
        # Store the menu category associated with its menu item number
        menu_items[i] = key # Add the menu item number and menu item name to
        # Add 1 to the menu item number
        i += 1 # This will be used to number the menu items

    print() # Print a blank line

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is equal to 5, if so, exit the program
    if menu_category == "5": # Check if the customer's input is equal to 5, if so, exit the program
        # Exit the program
        print() # Print a blank line
        print("Thank you for dining with us!")
        exit() # Exit the program


    # 6. Check if the customer's input is a number
    if menu_category.isdigit(): # Check if the customer's input is a number
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys(): # Check if the customer's input is a valid option
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)] # Save the menu category name to a variable
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}") # Print out the menu category name they selected
            print() # Print a blank line

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?") # Print out the menu options from the menu_category_name
            print() # Print a blank line

            i = 1 # This will be used to number the menu items
            menu_items = {} # This will be used to store the menu items
            print("Item # | Item name                | Price") # Print the menu item number, menu item name, and menu item price
            print("-------|--------------------------|-------") # Print a line to separate the menu item number, menu item name, and menu item price
            for key, value in menu[menu_category_name].items(): # Loop through the menu dictionary
                
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict: # Check if the menu item is a dictionary to handle differently
                    for key2, value2 in value.items(): # Loop through the menu dictionary
                        num_item_spaces = 24 - len(key + key2) - 3 # Calculate the number of spaces for formatted printing
                        item_spaces = " " * num_item_spaces # Create space strings
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}") # Print the menu item number, menu item name, and menu item price
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key, 
                        "Price": value
                    } # Add the menu item number and menu item name to
                    i += 1 # This will be used to number the menu items
            
            print() # Print a blank line

            # Ask customer to input menu item number
            menu_item_number = input("Type menu item number: ") # Ask customer to input menu item number
            print() # Print a blank line

            # 3. Check if the customer typed a number and if it is in the menu items
            if menu_item_number.isdigit() and int(menu_item_number) in menu_items.keys(): # Check if the customer typed a number and if it is in the menu items
                # Store the menu item name as a variable
                menu_item_name = menu_items[int(menu_item_number)]["Item name"]
                # Ask the customer for the quantity of the menu item
                menu_item_quantity = input(f"How many {menu_item_name}'s would you like to order? (default is 1): ") # Ask the customer for the quantity of the menu item
                print() # Print a blank line

                # Check if the quantity is a number, default to 1 if not
                if menu_item_quantity.isdigit(): # Check if the quantity is a number, default to 1 if not
                    menu_item_quantity = int(menu_item_quantity) # Convert the quantity to an integer
                else:
                    menu_item_quantity = 1
                # Add the item name, price, and quantity to the order list
                order_list.append({
                    "Item name": menu_item_name,
                    "Price": menu_items[int(menu_item_number)]["Price"],
                    "Quantity": menu_item_quantity
                })
                           
    # 7. Return the order list
    def get_order_list(order_list):

        # Loop through the items in the customer's order
        for item in order_list: # Loop through the items in the customer's order
            # Store the dictionary items as variables
            item_name = item["Item name"]
            item_price = item["Price"]
            item_quantity = item["Quantity"]
            # Calculate the number of spaces for formatted printing
            num_item_spaces = 24 - len(item_name) - 3
            # Create space strings
            item_spaces = " " * num_item_spaces

        # Calculate the cost of the order using list comprehension
        # Multiply the price by quantity for each item in the order list, then sum()
        # and print the prices.
        
        return order_list

# Call the function with the order_list

    
    # Calculate the cost of the order using list comprehension
    # Multiply the price by quantity for each item in the order list, then sum()
    # and print the prices.
    total = sum([item["Price"] * item["Quantity"] for item in order_list]) # Calculate the cost of the order using list comprehension
    print(f"Sub-total: ${total:.2f}") # Print the total cost of the order
    print() # Print a blank line

    # Ask the customer if they would like to order anything else
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ") # Ask the customer if they would like to order anything else
    # Check the customer's input
    match keep_ordering.lower():
        case 'y':
            continue
        case 'n':
            place_order = False
        case _:
            print("Please try again.")
            continue

 # here is where we will ask the customer if they would like to order anything else
   

# 11. Calculate the cost of the order using list comprehension

# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.


# Print the order
print("Your order:") # Print the order
print() # Print a blank line

print("Item name                 | Price | Quantity")
print("--------------------------|-------|----------")
for item in order_list:
    item_name = item["Item name"] # Store the dictionary items as variables
    item_price = item["Price"] # Store the dictionary items as variables
    item_quantity = item["Quantity"] # Calculate the number of spaces for formatted printing
    num_item_spaces = 24 - len(item_name) + 1 # Create space strings 
    item_spaces = " " * num_item_spaces
    print(f"{item_name}{item_spaces} | ${item_price} | {item_quantity}")

print() # Print a blank line

#calculate total order price using list comprehension
total = sum([item["Price"] * item["Quantity"] for item in order_list]) # Calculate the cost of the order using list comprehension
print(f"Total: ${total:.2f}") # Print the total cost of the order


# Ask the customer is they would like a text alert when their order is ready
print() # Print a blank line
text_alert = input("Would you like a text alert when your order is ready? note - requires text opt in (Y)es or (N)o ") # Ask the customer is they would like a text alert when their order is ready
# Check the customer's input
match text_alert.lower():
    case 'y':
        input("Please enter your phone number: (xxx) xxx-xxxx ")
        print("Thank you for opting in to receive text alerts!")
    case 'n':
        print("Thank you for your order!")
    case _:
        print("Please try again.")
        print() # Print a blank line

        # Exit the program
        print() # Print a blank line
        print(f"Thank you for dining with us, {customer_name}!") 
        print()# Exit the program

print() # Print a blank line



# Exit the program
print() # Print a blank line
print(f"Thank you for dining with us, {customer_name}!") 
print()# Exit the program

