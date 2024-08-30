class MENU:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.menu_item = {
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


    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}ml")
        # print(f"Money: ${profit}")

    def is_resource_sufficient(self, drink_ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink_ingredients:
            if self.resources[item] < drink_ingredients[item]:
                print(f"Sorry, there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, drink_name):
        """Deduct the required ingredients from the resources."""
        ingredients = self.menu_item[drink_name]["ingredients"]
        if self.is_resource_sufficient(ingredients):
            for item in ingredients:
                self.resources[item] -= ingredients[item]
            print(f"Here is your {drink_name} ☕️. Enjoy!")
        else:
            print(f"Cannot make {drink_name} due to insufficient resources.")

    def get_ingredients(self, drink_name):
        """Return the ingredients for a specific drink."""
        return self.menu_item[drink_name]["ingredients"]

    def list_drinks(self):
        """List all available drinks."""
        return list(self.menu_item.keys())

# Example usage:
menu = MENU()


# Listing all available drinks
print("Available Drinks:", menu.list_drinks())

# Making a coffee
# menu.make_coffee("latte")

# Print resources after making a coffee
menu.report()
