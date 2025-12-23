from datetime import datetime

# define the menu items for a restaurant
menu_items = {"STARTERS" : {"Poha":40 , "Grilled Corn":35, "Chilli Paneer":50}}
menu_items["MAIN COURSE"] = {"Maharaja Thali":350, "Special Thali":230, "Restro Special Thali":300}
menu_items["DESSERTS"] = {"Gulab Jamun":80, "Rasgulla":70, "Ice Cream":60}
menu_items["BEVERAGES"] = {"Cold Coffee":50, "Lemonade":30, "Special Tea":40}
# function to display the menu
def display_menu():
    print("--------------- RESTRO MENU ---------------")

print("--------------- RESTRO MENU ---------------")

# display the menu
for category, items in menu_items.items():
    print(f"\n{category}:")
    print()
    for item, price in items.items():
        print(f"  {item:<30} ₹{price}")

# interactive ordering: ask customer for items and check availability
order_total = 0
order_items = []
print()
print("Please enter the item name to order. Press Enter with no input to finish.")
done = False
while True:
    choice = input("Item name: ")
    if choice == "":
        break
    # case-insensitive search for the item across categories
    found = False
    for items in menu_items.values():
        for name, price in items.items():
            if name.lower() == choice.lower():
                found = True
                qty_str = input("Quantity (default 1): ")
                try:
                    qty = int(qty_str) if qty_str != "" else 1
                    if qty <= 0:
                        qty = 1
                except ValueError:
                    qty = 1
                order_total += price * qty
                order_items.append((name, qty, price, price * qty))
                # show current total and greet
                print(f"Current order total: ₹{order_total}")
                # ask if the customer wants to order anything else
                more = input("Anything else you want to order? (y/n): ").strip().lower()
                if more in ("n", "no"):
                    done = True
                    break
        if found:
            break
    if not found:
        print("Item not available. Please try again.")
    if done:
        break

print()
# print professional bill inside a framed table with aligned columns
print("+" + "=" * 62 + "+")
title = "RESTRO BILL"
print("|" + title.center(62) + "|")
print("+" + "=" * 62 + "+")
print(f"| Date: {datetime.now().strftime('%d-%b-%Y %H:%M:%S'):<54} |")
print("+" + "-" * 62 + "+")

# column format: No | Item (25) | QTY | Rate | Line Total
row_fmt = "| {:>2} | {:<25} | {:>3} | {:>7} | {:>11} |"
line_len = len(row_fmt.format(1, 'Item name', 1, 'Rate', 'Line Total'))
border = "+" + "-" * (line_len - 2) + "+"
print(border)
print(row_fmt.format('No', 'Item', 'Qty', 'Rate', 'Line Total'))
print(border)
if order_items:
    for idx, (name, qty, rate, line) in enumerate(order_items, start=1):
        print(row_fmt.format(idx, name[:25], qty, rate, line))
else:
    empty_row = "|" + " " * (line_len - 2) + "|"
    print(empty_row)
print(border)
total_str = f"₹{order_total}"
print("|" + f"{'Total':>46} {total_str:>14}" + " |")
print("+" + "=" * (line_len - 2) + "+")
print("Thank you! Come again.")


