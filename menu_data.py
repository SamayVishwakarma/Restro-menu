from datetime import datetime

# define the menu items for a restaurant (data only)
menu_items = {
    "STARTERS": {"Poha": 40, "Grilled Corn": 35, "Chilli Paneer": 50},
    "MAIN COURSE": {"Maharaja Thali": 350, "Special Thali": 230, "Restro Special Thali": 300},
    "DESSERTS": {"Gulab Jamun": 80, "Rasgulla": 70, "Ice Cream": 60},
    "BEVERAGES": {"Cold Coffee": 50, "Lemonade": 30, "Special Tea": 40},
}

# helper to get a flat list if needed
def get_all_items():
    for category, items in menu_items.items():
        for name, price in items.items():
            yield category, name, price

if __name__ == '__main__':
    # simple print when run directly
    print('Menu data module — import from app, do not run directly')
