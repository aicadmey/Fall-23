def read_menu_data(file_path):
    menu = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                item, price = line.strip().split(': ')
                menu[item] = float(price)
    except FileNotFoundError:
        print(f"Menu data file not found at {file_path}.")
    return menu

def calculate_total_order_cost(menu, order):
    total_cost = 0
    for item, quantity in order.items():
        if item in menu:
            total_cost += menu[item] * quantity
        else:
            print(f"Item '{item}' not found in the menu.")
    return total_cost

try:
    menu_data = read_menu_data('menu.txt')  # Use the correct file path to 'menu.txt'

    order = {}
    while True:
        item = input("Enter an item from the menu (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        quantity = int(input(f"Enter the quantity for {item}: "))
        order[item] = quantity

    total_cost = calculate_total_order_cost(menu_data, order)
    print(f"Total order cost: ${total_cost:.2f}")

except KeyboardInterrupt:
    print("\nOrder canceled.")
