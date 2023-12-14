# UNC AI Bootcamp Week 2 Homework 

## Challenge Instructions

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


# Launch the store and present a greeting to the customer
print() # Print a blank line

# 2. Ask the customer for their name and store it in a variable
def welcome_customer():
    name = input("What is your name? ")
    return name

print("Welcome to the variety food truck.") # \n is a new line character
print() # Print a blank line

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? (Choose 5 to exit.)") 
    print() # Print a blank line
    
    # Create a variable for the menu item number
    i = 1 # This will be used to number the menu items

    # Create a dictionary to store the menu for later retrieval
    menu_items = {} # This will be used to store the menu items

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
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


    # Check if the customer's input is a number
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
                           
    # Return the order list
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
    order_list = get_order_list(order_list)

    # Tell the customer their current order
    print("Your order so far:") # Tell the customer their current order
    print() # Print a blank line

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
        # Print the item name, price, and quantity
        print(f"{item_name}{item_spaces} | ${item_price} | {item_quantity}")
    print() # Print a blank line
    
    # Calculate the cost of the order using list comprehension
    # Multiply the price by quantity for each item in the order list, then sum()
    # and print the prices.
    total = sum([item["Price"] * item["Quantity"] for item in order_list]) # Calculate the cost of the order using list comprehension
    print(f"Sub-total: ${total:.2f}") # Print the total cost of the order
    print() # Print a blank line

    # Ask the customer if they would like to order anything else
    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ") # Ask the customer if they would like to order anything else
    # Check the customer's input
    if keep_ordering.lower() == "y": # Check the customer's input
        # Keep ordering
        continue
    elif keep_ordering.lower() == "n": # Check the customer's input
        # Exit the keep ordering question loop
        place_order = False
    else:
        # Tell the customer to try again
        print("Please try again.")


        # Complete the order
        # Since the customer decided to stop ordering, thank them for their order
        print() # Print a blank line
        print("Thank you for your order! Here is your total:") # Since the customer decided to stop ordering, thank them for their order
        print() # Print a blank line

        # Calculate the cost of the order using list comprehension
        # Multiply the price by quantity for each item in the order list, then sum() and print the prices.
        print("Your Total Order:") # Print the order
        print() # Print a blank line
        print("Item name                 | Price | Quantity")
        print("--------------------------|-------|----------")
        # Add your code here
        pass
        # Tell the customer to try again
        print("Please try again.")


        # Complete the order
        # Since the customer decided to stop ordering, thank them for their order
print() # Print a blank line
print("Thank you for your order! Here is your total:") # Since the customer decided to stop ordering, thank them for their order
print() # Print a blank line

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

print() # Print a blank line

# Thank the customer for their order and let them know when it will be ready
print("Thank you for your order! It will be ready in 10 minutes.") # Thank the customer for their order and let them know when it will be ready
# Ask the customer is they would like a text alert when their order is ready
print() # Print a blank line
text_alert = input("Would you like a text alert when your order is ready? (Y)es or (N)o ") # Ask the customer is they would like a text alert when their order is ready
# Check the customer's input
if text_alert.lower() == "y": # Check the customer's input
    # Thank the customer for opting in to receive text alerts
    print("Thank you for opting in to receive text alerts!") # Thank the customer for opting in to receive text alerts
elif text_alert.lower() == "n": # Check the customer's input
    # Thank the customer for their order
    print("Thank you for your order!") # Thank the customer for their order
else:
    # Tell the customer to try again
    print("Please try again.")
    
# Ask the customer if they would like to opt in to receive text alerts for promotions and discounts
# Ask the customer how they would like to pay
# Ask the customer if they would like to leave a tip
# Ask the customer if they would like to receive a receipt


# Exit the program
print() # Print a blank line
print("Thank you for dining with us!") # Exit the program

