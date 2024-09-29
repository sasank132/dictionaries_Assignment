import data
import functions

def show_main_menu():
    """
    Main function to display the menu and handle user interactions.
    """
    current_order = []
    
    while True:
        # Display the main menu
        print("\nWelcome to Sasank's Diner")
        print("___________________________")
        print('N - Start a new order')
        print('C - Change the current order')
        print('X - Close the order and print the check')
        print('R - Reset the order')
        print('Q - Quit')
        
        # Get user's menu choice
        user_menu_choice = input('Your choice: ').strip().upper()
        
        # Handle different user choices
        if user_menu_choice == 'Q':
            print("Exiting... Goodbye!")
            break
        elif user_menu_choice == 'X':
            print('Closing the order and printing the check...')
            print_check(current_order)
        elif user_menu_choice == 'C':
            current_order = change_order(current_order)
        elif user_menu_choice == 'N':
            print('Starting a new order...')
            while input('Would you like to add a dish? (y/n): ').strip().lower() == 'y':
                item_code, quantity = input("Enter item code and quantity (e.g., E1 2): ").split()
                if functions.process_customer_request(data.menu_dict, item_code, int(quantity)):
                    current_order.append((item_code, int(quantity)))
                else:
                    print("Invalid item code or insufficient stock.")
        elif user_menu_choice == 'R':
            print("Resetting the current order...")
            current_order = []
        else:
            print("Invalid choice. Please choose a valid option.")

def print_check(current_order):
    """
    Prints the final check with order details including item prices and totals.
    """
    if not current_order:
        print("Your order is empty.")
        return
    
    print("\nYour Order Summary:")
    total = 0
    tax_rate = 0.07  # 7% tax
    
    for item_code, quantity in current_order:
        item = next((i for i in data.menu_dict if i["code"] == item_code), None)
        if item:
            item_total = item["price"] * quantity
            total += item_total
            print(f"{item['name']} (x{quantity}) - ${item_total}")
    
    tax = total * tax_rate
    grand_total = total + tax
    
    print(f"\nSubtotal: ${total:.2f}")
    print(f"Tax (7%): ${tax:.2f}")
    print(f"Grand Total: ${grand_total:.2f}")
    print("\nThank you for dining at Sasank's Diner!")

def change_order(current_order):
    """
    Allows the user to modify the current order.
    """
    if not current_order:
        print("No items in the current order to change.")
        return current_order
    
    print("\nCurrent order:")
    for idx, (item_code, quantity) in enumerate(current_order, 1):
        item = next((i for i in data.menu_dict if i["code"] == item_code), None)
        if item:
            print(f"{idx}. {item['name']} (x{quantity})")
    
    option = input("Would you like to remove an item? (y/n): ").strip().lower()
    if option == 'y':
        item_number = int(input("Enter the item number to remove: "))
        if 0 < item_number <= len(current_order):
            removed_item = current_order.pop(item_number - 1)
            print(f"Removed {removed_item[0]} from your order.")
        else:
            print("Invalid item number.")
    else:
        print("No items were removed.")
    
    return current_order

if __name__ == '__main__':
    # Initialize the item categories (if needed)
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    desserts = []
    
    # Start the main menu interface
    show_main_menu()
