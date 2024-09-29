import random

# Data for the menu items
menu_items = [
    'D1   SODA 3', 'D2   LEMONADE 3', 'D3   TEA 2', 'D4 WATER 1',
    'A1   POTATO_CAKES 7', 'A2   SPINACH_DIP 5', 'A3   OYSTERS 13', 
    'A4   CHEESE_FRIES 4', 'A5   ONION_RINGS 7',
    'S1   COBB 14', 'S2   CAESAR 13', 'S3   GREEK 12',
    'E1   BURGER 16', 'E2   PASTA 15', 'E3   GNOCCHI 14', 
    'E4   GRILLED_STEAK_SANDWICH 17',
    'T1   CARAMEL_CHEESECAKE 13', 'T2   APPLE_COBBLER 12', 'T3   BROWNIE_SUNDAE 9', 'T4   FLAN 8'
]

# Categories of menu items
drink_items = ['D1', 'D2',  'D3', 'D4']
appetizer_items = ['A1', 'A2',  'A3', 'A4', 'A5']
salad_items = ['S1', 'S2', 'S3']
entree_items = ['E1', 'E2',  'E3', 'E4']
dessert_items = ['T1', 'T2',  'T3', 'T4']

# Combining all items into one list
all_items = drink_items + appetizer_items + salad_items + entree_items + dessert_items

# Function to determine stock based on item type
def get_stock(item_code):
    if item_code in drink_items:
        return random.randint(3000, 10000)  # Large stock for drinks
    else:
        return random.randint(25, 50)  # Random stock for non-drink items

# Convert the list of menu items to a list of dictionaries
menu_dict = []
for item in menu_items:
    code, name, price = item.split(maxsplit=2)
    menu_dict.append({
        "code": code,
        "name": name,
        "price": int(price),
        "stock": get_stock(code)
    })

# Printing the resulting menu dictionary (for testing purposes)
for item in menu_dict:
    print(item)
