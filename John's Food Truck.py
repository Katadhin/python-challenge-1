# Menu dictionary
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
order_list = []

# Welcome Customer
print("Welcome to John's Food Truck! \n") # \n is a new line character
print() # Print a blank line

# Bonus - Ask for Customer Name
customer_name = input("What is your name? ")


def greet_customer(name):
    print(f"Hello, {name}! Select a menu to start your order") # f-string
    print()

def menu_selection (menu):
    for key in menu:
        print(key)
    print("5 to Exit")
    print()
    
# Present Menu
while True:
    print("Please choose a category:")
    print()
    for i, category in enumerate(menu.keys(), 1):
        print(f"{i}. {category}")

    print()    

    # Customer Category Selection
    category_choice = input("Enter the number of the category you'd like to order from (or 5 to exit): ")

print()

if category_choice == '5':
    print("Thank you for dining with us!")
    # Loop Through Categories
    print(f"{selected_category} Menu:")
    max_item_width = max(len(item) for item in menu[selected_category].keys())  # Find the maximum item name width

    for i, item in enumerate(menu[selected_category].keys(), 1):
        price = menu[selected_category][item]
        price_formatted = f"${price:.2f}"  # Format the price to 2 decimal places
        print(f"{i}. {item:<{max_item_width}} - {price_formatted} each")

    while True:
        item_choice = input(f"Enter the number of the {selected_category} item you want to order (or 'done' to finish): ")

        if item_choice.lower() == 'done':
            break

        if item_choice.isdigit():
            item_choice = int(item_choice)
            if 1 <= item_choice <= len(menu[selected_category]):
                selected_item = list(menu[selected_category].keys())[item_choice - 1]
                quantity = input(f"How many {selected_item} would you like to order? (default is 1): ")
                if quantity.isdigit():
                    quantity = int(quantity)
            else:
                print("Invalid item number. Please try again.")
        else:
            print("Invalid input. Please enter a number or 'done'.")


    # Loop Through Categories
    print(f"{selected_category} Menu:")
    max_item_width = max(len(item) for item in menu[selected_category].keys())  # Find the maximum item name width

    for i, item in enumerate(menu[selected_category].keys(), 1):
        price = menu[selected_category][item]
        price_formatted = f"${price:.2f}"  # Format the price to 2 decimal places
        print(f"{i}. {item:<{max_item_width}} - {price_formatted} each")

    while True:
        item_choice = input(f"Enter the number of the {selected_category} item you want to order (or 'done' to finish): ")

        if item_choice.lower() == 'done':
            break

        if item_choice.isdigit():
            item_choice = int(item_choice)
            if 1 <= item_choice <= len(menu[selected_category]):
                selected_item = list(menu[selected_category].keys())[item_choice - 1]
                quantity = input(f"How many {selected_item} would you like to order? (default is 1): ")
                if quantity.isdigit():
                    quantity = int(quantity)
                else:
                    quantity = 1

                order_list.append({
                    "Item name": selected_item,
                    "Price": menu[selected_category][selected_item],
                    "Quantity": quantity
                })
            else:
                print("Invalid item number. Please try again.")
        else:
            print("Invalid input. Please enter a number.")

    # Give Customer Order
    print("Your order:")
    total_price = 0
    for item in order_list:
        print(f"{item['Item name']} x{item['Quantity']} - ${item['Price']:.2f} each")
        total_price += item['Price'] * item['Quantity']

    print(f"Total Price: ${total_price:.2f}")

    # Bonus - Offer Discount for Large Order
    if total_price >= 20:
        discount = total_price * 0.1  # 10% discount
        total_price -= discount
        print(f"You qualify for a 10% discount! Your new total is ${total_price:.2f}")

    # Bonus - Ask for Payment Type
    payment_choice = input("How would you like to pay? (Cash, Credit Card, or Mobile Payment): ")

    # Bonus - Give customer estimate wait time based on # of orders
    num_orders = len(order_list)
    if num_orders > 0:
        wait_time = num_orders * 5  # 5 minutes per order
        print(f"Your estimated wait time is {wait_time} minutes.")
    else:
        print("You didn't place an order.")

    # Bonus - Ask customer if they would like a text alert - Opt in for marketing
    text_alert = input("Would you like to receive a text alert for promotions and discounts? (Yes or No): ")
    if text_alert.lower() == 'yes':
        print("Thank you for opting in to receive text alerts for promotions and discounts.")
    else:
        print("You have chosen not to receive text alerts.")

    print("Thank you for dining with us!")
