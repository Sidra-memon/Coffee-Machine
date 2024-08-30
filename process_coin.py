class Coin():
    currency = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    def __init__(self):
        self.profit = 0
        self.total_amount = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.currency}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        total_amount = int(input("Please enter money: "))
        # print(f"${total}")
        total_amount = int(input("how many quaters?"))*0.25
        total_amount += int(input("how many dimes?")) * 0.1
        total_amount += int(input("how many nickels?")) * 0.05
        total_amount += int(input("how many pennies?")) * 0.01
        return total_amount

    def is_transaction_successful(self, dirnk_cost):
        """Return true when payment is accepted,and false when money is insufficent """
        if self.total_amount >= dirnk_cost:
            change = round(self.total_amount - dirnk_cost, 2)
            print(f"here is your ${change} change")
            self.profit += dirnk_cost
            self.total_amount = 0
            return True
        else:
            print("Sorry!Insufficient Amount")
            return False