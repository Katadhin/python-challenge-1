# Food Truck Ordering System
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
order_list = []

# Print menu
def print_menu(menu):
    for key, value in menu.items():
        print(key)
        if isinstance(value, dict):
            for key2, value2 in value.items():
                print("\t", key2)
                if isinstance(value2, dict):
                    for key3, value3 in value2.items():
                        print("\t\t", key3, ":", value3)
                else:
                    print("\t\t", value2)
        else:
            print("\t", value)

# Print receipt
def print_receipt(order_list):
    total = 0
    print("Your order:")
    for item in order_list:
        print("\t", item["Item name"], ":", item["Quantity"], "x", item["Price"])
        total += item["Quantity"] * item["Price"]
    print("Total:", total)

# Order



# Order System

# Create an empty list. This list will later store a customer's order in dictionary format, as follows:
[
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
]