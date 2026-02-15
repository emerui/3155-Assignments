### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese":24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient in ingredients.keys():
            if ingredients[ingredient] > self.machine_resources[ingredient]:
                print ("Sorry not enough", ingredient)
                return False
        return True
    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input(how many quarters?: )"""
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

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, amount in recipes[sandwich_size][order_ingredients].items():
            self.machine_resources[ingredient] -= amount
        print(sandwich_size, "sandwich is ready. Bon apetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###
Sandwich = SandwichMachine(resources)
while True:
    print("Hello, what sandwich would you like? (Large, Medium, Small, off , Report)")
    n = input().lower().strip()
    if n == "report":
        for resource in Sandwich.machine_resources:
            if resource == "cheese":
                print("There are ", Sandwich.machine_resources[resource], "cheese pound(s) left")
                continue
            print("There are ", Sandwich.machine_resources[resource], " ", resource, " slice(s) left")
        continue
    if n == "off":
        break
    if n != "large" and n != "medium" and n != "small":
        print("not an option")
        continue
    cost = recipes.get(n).get("cost")
    if n == "large":
        if Sandwich.check_resources(recipes.get("large").get("ingredients")):
            print("You owe", cost)
            if not Sandwich.transaction_result(cost, Sandwich.process_coins()):
                continue
            else:
                Sandwich.make_sandwich(n, "ingredients")

    if n == "medium":
        if Sandwich.check_resources(recipes.get("medium").get("ingredients")):
            print("You owe", cost)
            if not Sandwich.transaction_result(cost, Sandwich.process_coins()):
                continue
            else:
                Sandwich.make_sandwich(n, "ingredients")

    if n == "small":
        if Sandwich.check_resources(recipes.get("small").get("ingredients")):
            print("You owe", cost)
            if not Sandwich.transaction_result(cost, Sandwich.process_coins()):
                continue
            else:
                Sandwich.make_sandwich(n, "ingredients")
