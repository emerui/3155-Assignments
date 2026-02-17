class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("please insert whole integer coins")
        while True:
            try:
                large = int(input("how many  large dollars: "))
                break
            except:
                pass
            print("please insert whole integers; try again")

        while True:
            try:
                half = int(input("how many half dollars: "))
                break
            except:
                pass
            print("please insert whole integers; try again")

        while True:
            try:
                quarter = int(input("how many quarters: "))
                break
            except:
                pass
            print("please insert whole integers; try again")

        while True:
            try:
                nickle = int(input("how many nickles: "))
                break
            except:
                pass
            print("please insert whole integers; try again")

        return large + (half / 2) + (quarter / 4) + (nickle / 10)
    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins > cost:
            print("Sorry that is not enough. Money refunded")
            return False
        else:
            print("Here is $", cost - coins, " in change")
            return True
