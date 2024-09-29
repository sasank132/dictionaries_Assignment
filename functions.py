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


# Display the menu items
def display_menu(menu):
    for item in menu:
        print(f"{item['code']} - {item['name']} - ${item['price']} (Stock: {item['stock']})")
