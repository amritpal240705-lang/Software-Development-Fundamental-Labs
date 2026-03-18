
# Global variables
inventory = {}
item_id_counter = 1000


# Task 1: Add Inventory Item
def add_inventory_item():
    global item_id_counter

    print("\nAdding Inventory Item:\n")

    name = input("Item Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per Item: $"))

    item_id = item_id_counter
    item_id_counter += 1

    inventory[item_id] = [name, quantity, price]

    print("\nItem Name:", name)
    print("Item ID:", item_id)
    print("Quantity:", quantity)
    print("Price per Item: $%.2f" % price)

    return name, item_id, quantity, price


# Task 2: Calculate Total Value
def calculate_total_value():
    name, item_id, quantity, price = add_inventory_item()

    total = quantity * price

    print("\nTotal Value: $%.2f" % total)

    return total

calculate_total_value()