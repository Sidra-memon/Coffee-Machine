from check_resource import Resource
resource = Resource()
class MENU():
    def __init__(self,resource):
        self. menu_item = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


    def get_menu(self):
         """Return the entire menu."""
         return self.menu_item

resource = Resource()
menu = MENU(resource)

# Accessing the entire menu
print("Menu:", menu.get_menu())
# Accessing ingredients for a specific drink
print("Latte Ingredients:", menu.get_ingredients("latte"))



