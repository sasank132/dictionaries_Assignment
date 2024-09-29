# manager to update the menu items
def update_menu_item(menu, code, field, new_value):
    pass


def add_menu_item(menu, code, name, price, stock):
    pass

def remove_menu_item(menu, code):
    pass

# handle customer requests and verify stock availability
def process_customer_request(menu, request_code, quantity):
    
    quantity = int(quantity)
    for item in menu:
        if item['code'] == request_code:
            if item['stock'] >= quantity:
                item['stock'] -= quantity  # Reduce the stock
                print(f"{quantity} x {item['name']} ordered. Stock remaining: {item['stock']}")
                return True
            else:
                print(f"Not enough stock for {item['name']}. Available: {item['stock']}, Requested: {quantity}")
                return False
    print(f"Item {request_code} not found on the menu.")
    return False

# Update an existing menu item (either price or name)
def update_menu_item(menu, code, field, new_value):
    for item in menu:
        if item['code'] == code:
            if field == 'name':
                item['name'] = new_value
            elif field == 'price':
                item['price'] = int(new_value)
            print(f"{code} updated: {field} changed to {new_value}")
            return True
    print(f"Item {code} not found.")
    return False

# Add a new menu item
def add_menu_item(menu, code, name, price, stock):
    new_item = {"code": code, "name": name, "price": int(price), "stock": int(stock)}
    menu.append(new_item)
    print(f"Added new item: {new_item}")

# Remove an item from the menu
def remove_menu_item(menu, code):
    for item in menu:
        if item['code'] == code:
            menu.remove(item)
            print(f"Removed item: {code}")
            return True
    print(f"Item {code} not found.")
    return False

def take_customer_request(menu):
    request_code = input("Enter the code of the item you want to order: ").upper()
    quantity = input(f"Enter the quantity of {request_code} you want to order: ")

    if not quantity.isdigit():
        print("Invalid quantity. Please enter a number.")
        return

    quantity = int(quantity)
    
    if not process_customer_request(menu, request_code, quantity):
        print("Order could not be processed.")
    else:
        print(f"{quantity} {request_code} successfully ordered.")
# Display the menu items
def display_menu(menu):
    for item in menu:
        print(f"{item['code']} - {item['name']} - ${item['price']} (Stock: {item['stock']})")
